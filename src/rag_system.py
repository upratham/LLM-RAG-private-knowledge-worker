from openai import OpenAI
from langchain_community.llms import Ollama
from langchain_core.messages import SystemMessage, HumanMessage



# Initialize Llama 3.2 via Ollama

ollama_host = "http://localhost:11434"  # Adjust if your Ollama server is running on a different URL or port
ollama_base_url = f"{ollama_host}/v1"
ollama_model="llama3.2"
ollama_client = OpenAI(base_url=ollama_base_url, api_key="ollama")
llm = Ollama(model="llama3.2", base_url=ollama_host, temperature=0)

from pydantic import BaseModel,Field

class RankOrder(BaseModel):
   order: list[int] = Field(description="he order of relevance of chunks, from most relevant to least relevant, by chunk id number")

def rerank(question, chunks):
    system_prompt = """
You are a document re-ranker.
You are provided with a question and a list of relevant chunks of text from a query of a knowledge base.
The chunks are provided in the order they were retrieved; this should be approximately ordered by relevance, but you may be able to improve on that.
You must rank order the provided chunks by relevance to the question, with the most relevant chunk first.
Reply only with the list of ranked chunk ids, nothing else. Include all the chunk ids you are provided with, reranked.
strictly reply do not leave the order empty and do not add or remove any chunk ids.
"""
    user_prompt = f"The user has asked the following question:\n\n{question}\n\nOrder all the chunks of text by relevance to the question, from most relevant to least relevant. Include all the chunk ids you are provided with, reranked.\n\n"
    user_prompt += "Here are the chunks:\n\n"
    for index, chunk in enumerate(chunks):
        user_prompt += f"# CHUNK ID: {index + 1}:\n\n{chunk.page_content}\n\n"
    user_prompt += "Reply only with the list of ranked chunk ids, nothing else."
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    response = ollama_client.chat.completions.parse(
        model="llama3.1",
        messages=messages,
        response_format=RankOrder,
    )
    parsed = response.choices[0].message.parsed
    order = parsed.order
    return [chunks[i - 1] for i in order if isinstance(i, int) and 1 <= i <= len(chunks)]



def fetch_unranked_chunks(question, retriever):
    relevant_chunks = retriever.invoke(question)
    return relevant_chunks


def rewrite_query(question, history=[]):
    """Rewrite the user's question into a focused knowledge-base search query."""
    message = f"""
You are a query rewriter for a private knowledge base assistant.
You help answer questions about the user profile (education, experience, skills, projects, achievements, and documents) stored in the knowledge base.
You will receive the conversation history and the user's latest question.
Rewrite the question into a short, specific search query that is most likely to retrieve the right chunks.

Conversation history:
{history}

Rules:
- Output only the rewritten query, nothing else.
- Keep it short, precise, and concrete.
- Do not mention document names, file paths, or the knowledge base.
- If the question asks about a person, include their full name if known; otherwise keep the subject generic.
"""
    reresponse = llm.invoke([SystemMessage(content=message), HumanMessage(content=question)])
    return reresponse

def merge_chunks(chunks, reranked):
    merged = chunks[:] 
    existing = [chunk.page_content for chunk in chunks]
    for chunk in reranked:
        if chunk.page_content not in existing:
            merged.append(chunk)
    return merged

