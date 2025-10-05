#python -m my_first.main gradio
import time
import gradio as gr
from datetime import datetime
from dotenv import load_dotenv
from my_first.crew import MyFirst

load_dotenv()

def run_crew(topic: str):
    if not topic.strip():
        return "Please provide a topic to start the research."
    inputs = {"topic": topic}#, "current_year": str(datetime.now().year)}
    try:
        result = MyFirst().crew().kickoff(inputs=inputs)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

def launch_gradio_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# AI Agent 💭")
        
        chat = gr.Chatbot(label="CrewAI Chat", type="messages")
        msg_input = gr.Textbox(placeholder="Type your topic here...", lines=1, show_label=False)
        state = gr.State([])

        def process_message(msg, chat_history):
            if not msg.strip():
                return "", chat_history, chat_history

            chat_history.append({"role": "user", "content": msg})
            yield "", chat_history, chat_history
            
            thinking_message = {"role": "assistant", "content": "."}
            chat_history.append(thinking_message)
            yield "", chat_history, chat_history

            dots = [".  ", ".. ", "..."]

            response_ready = False
            from threading import Thread

            def generate_response():
                nonlocal response_ready, final_response
                final_response = run_crew(msg)
                response_ready = True

            final_response = ""
            thread = Thread(target=generate_response)
            thread.start()

            i = 0
          
            start_time = time.time()
            while not response_ready:
                elapsed = time.time() - start_time
                chat_history[-1]["content"] = f"{elapsed:.1f} s ⏳ thinking {dots[i % 3]}"
                yield "", chat_history, chat_history
                i += 1
                time.sleep(0.5)


            chat_history[-1]["content"] = final_response
            yield "", chat_history, chat_history

        msg_input.submit(
            process_message,
            inputs=[msg_input, state],
            outputs=[msg_input, state, chat]
        )

    demo.launch()

if __name__ == "__main__":
    launch_gradio_ui()
