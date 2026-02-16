
from pathlib import Path
from src.retriever import get_retriever
from src.rag_system import rewrite_query,fetch_unranked_chunks,merge_chunks,rerank
from tenacity import retry, wait_exponential
from openai import OpenAI
from langchain_community.llms import Ollama


def find_project_root(start: Path, markers=("pyproject.toml", ".git")) -> Path:
    cur = start.resolve()
    for p in [cur] + list(cur.parents):
        if any((p / m).exists() for m in markers):
            return p
    return cur

PROJECT_ROOT =find_project_root(Path(__file__))
ollama_host = "http://localhost:11434"  # Adjust if your Ollama server is running on a different URL or port
ollama_base_url = f"{ollama_host}/v1"
ollama_model="llama3.2"
ollama_client = OpenAI(base_url=ollama_base_url, api_key="ollama")
llm = Ollama(model="llama3.2", base_url=ollama_host, temperature=0)
db_path=Path(str(PROJECT_ROOT)) / "vectors"
retriever=get_retriever(db_path=db_path)
wait = wait_exponential(multiplier=1, min=10, max=240)
SYSTEM_PROMPT_TEMPLATE = """
You are a helpful, knowledgeable assistant with access to a user's personal knowledge base.
Your role is to answer questions about the user's background, experience, achievements, and projects based on provided context.

while answering questions:
- Dont refere any document.
- understand the nuance of the question and depend on that provide short or long detailed answer.
- Maintain a polite and friendly tone
- If information is not available in the provided context, clearly state that you don't have that information
- don't mention name of any document use it for your context only.
- While answering strictly do not mentionany reference also , like "as per document 1, document 2, according to knowledge base" etc.

Context:
{context}
"""

def _history_to_messages(history):
    msgs = []
    for pair in history or []:
        # pair can be tuple/list like (user, assistant) or [user, assistant]
        if not pair or len(pair) != 2:
            continue
        user_msg, assistant_msg = pair

        if user_msg:
            msgs.append({"role": "user", "content": str(user_msg)})
        if assistant_msg:
            msgs.append({"role": "assistant", "content": str(assistant_msg)})

    return msgs

def make_rag_messages(question, history, chunks):
    context = "\n\n".join(
        f"Extract from {chunk.metadata.get('source','unknown')}:\n{chunk.page_content}"
        for chunk in chunks
    )
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context)

    return (
        [{"role": "system", "content": system_prompt}]
        + _history_to_messages(history)
        + [{"role": "user", "content": question}]
    )

def fetch_context(original_question,retriever=retriever,top_k=8):
    rewritten_question = rewrite_query(original_question)
    chunks1 = fetch_unranked_chunks(original_question, retriever=retriever)
    chunks2 = fetch_unranked_chunks(rewritten_question, retriever=retriever)
    chunks = merge_chunks(chunks1, chunks2)
    reranked = rerank(original_question, chunks)
    return reranked[:top_k]



@retry(wait=wait)
def answer_question(question: str, history,retriever=retriever) -> tuple[str, list]:
    """
    Answer a question using RAG and return the answer and the retrieved context
    """
    chunks = fetch_context(question, retriever)
    messages = make_rag_messages(question, history, chunks)
    response = ollama_client.chat.completions.create(model=ollama_model, messages=messages)
    return response.choices[0].message.content, chunks
   