
import os
from pathlib import Path
from src.retriever import get_retriever
from src.rag_system import rewrite_query,fetch_unranked_chunks,merge_chunks,rerank
from tenacity import retry, wait_exponential
from openai import OpenAI
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from pypdf import PdfReader
from dotenv import load_dotenv
from src.tooling import record_user_details,record_unknown_question,tools,handle_tool_calls
load_dotenv(override=True)
openai_api_key=os.getenv("OPENAI_API_KEY")



name = "Prathamesh Uravane"

def find_project_root(start: Path, markers=("pyproject.toml", ".git")) -> Path:
    cur = start.resolve()
    for p in [cur] + list(cur.parents):
        if any((p / m).exists() for m in markers):
            return p
    return cur

PROJECT_ROOT =find_project_root(Path(__file__))
reader = PdfReader(PROJECT_ROOT / "data" / "LinkedIn_Profile.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text

with open(PROJECT_ROOT / "data" / "summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()
# ollama_host = "http://localhost:11434"  # Adjust if your Ollama server is running on a different URL or port
# ollama_base_url = f"{ollama_host}/v1"
# ollama_model="llama3.2"
# ollama_client = OpenAI(base_url=ollama_base_url, api_key="ollama")
# llm = Ollama(model="llama3.2", base_url=ollama_host, temperature=0)
MODEL_OPENAI = "gpt-4.1-nano"
llm_openai=ChatOpenAI(
    model_name=MODEL_OPENAI,  # or gpt-3.5-turbo
    temperature=0,
    api_key=openai_api_key

)

openai_client = OpenAI(api_key=openai_api_key)
db_path=Path(str(PROJECT_ROOT)) / "vectors"
retriever=get_retriever(db_path=db_path)
wait = wait_exponential(multiplier=1, min=10, max=240)
SYSTEM_PROMPT_TEMPLATE = """
You are acting as Prathamesh Uravane. You are answering questions about Prathamesh Uravane\
particularly questions related to Prathamesh Uravane's career, background, skills and experience. \
Your responsibility is to represent Prathamesh Uravane for interactions on the website as faithfully,interactively and politely as possible. \
You are given a context of Prathamesh Uravane's background. which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across you. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email ,name and notes and record it using your record_user_details tool.\
do not move forward until you recive all the email , name and notes details from the user."


while answering questions:
- Dont refer any document.
- understand the nuance of the question and depend on that provide short or long detailed answer.
- Maintain a polite and friendly tone
- If information is not available in the provided context, clearly state that you don't have that information
- don't mention name of any document use it for your context only.
- While answering strictly do not mentionany reference also , like "as per document 1, document 2, according to knowledge base" etc.

LinkedIn Profile:
{linkedin}
Summary:
{summary}
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
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(context=context, linkedin=linkedin, summary=summary)

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
    #response = openai_client.chat.completions.create(model=MODEL_OPENAI, messages=messages,tools=tools)
    done=False
    while not done:
        response = openai_client.chat.completions.create(model=MODEL_OPENAI, messages=messages, tools=tools)

        finish_reason = response.choices[0].finish_reason
        
        # If the LLM wants to call a tool, we do that!
         
        if finish_reason=="tool_calls":
            message = response.choices[0].message
            tool_calls = message.tool_calls
            results = handle_tool_calls(tool_calls)
            messages.append(message)
            messages.extend(results)
        else:
            done = True
    return response.choices[0].message.content
   