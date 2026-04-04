import os

import gradio as gr
from dotenv import load_dotenv
from src.RAG_pipeline import answer_question


# def format_context(context):
#     result = "<h2 style='color: #ff7800;'>Relevant Context</h2>\n\n"
#     for doc in context:
#         result += f"<span style='color: #ff7800;'>Source: {doc.metadata['source']}</span>\n\n"
#         result += doc.page_content + "\n\n"
#     return result


def chat(history):
    last_message = history[-1]["content"]
    prior = history[:-1]
    answer = answer_question(last_message, prior)
    history.append({"role": "assistant", "content": answer})
    return history

def main():
    def put_message_in_chatbot(message, history):
        return "", history + [{"role": "user", "content": message}]

    theme = gr.themes.Soft(font=["Inter", "system-ui", "sans-serif"])

    with gr.Blocks(title="Digital Twin - Prathamesh Uravane", theme=theme) as ui:
        gr.Markdown("# 🤖 Digital Twin - Prathamesh Uravane\nAsk me anything!")

        chatbot = gr.Chatbot(
            label="💬 Conversation", height=600, type="messages", show_copy_button=True
        )
        message = gr.Textbox(
            label="Your Question",
            placeholder="Ask anything...",
            show_label=False,
        )

        message.submit(
            put_message_in_chatbot, inputs=[message, chatbot], outputs=[message, chatbot]
        ).then(chat, inputs=chatbot, outputs=chatbot)

    ui.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))



if __name__ == "__main__":
    main()
