import gradio as gr
from orbit import Orbit


async def setup():
    orbit = Orbit()
    await orbit.setup()
    return orbit


async def process_message(orbit, message, success_criteria, history):
    results = await orbit.run_superstep(message, success_criteria, history)
    return results, orbit


async def reset():
    new_orbit = Orbit()
    await new_orbit.setup()
    return "", "", None, new_orbit


def free_resources(orbit):
    print("Cleaning up")
    try:
        if orbit:
            orbit.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")


def export_history(history):
    if not history:
        return ""
    content = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in history])
    return content


with gr.Blocks(title="Orbit", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("""
    <h1 style='text-align: center;'>🛰️ Orbit-AI</h1>
    <p style='text-align: center;'>Your Personal Aide, Powered by LangGraph</p>
    """)

    orbit = gr.State(delete_callback=free_resources)

    with gr.Row():
        chatbot = gr.Chatbot(label="Orbit", height=300, type="messages")

    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label=False, placeholder="Your request to the Orbit")
        with gr.Accordion("Advanced Options", open=False):
            success_criteria = gr.Textbox(
                show_label=True,
                label="Success Criteria",
                placeholder="What are your success criteria?"
            )

    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")
        download_btn = gr.DownloadButton("Download Chat", visible=False)

    ui.load(setup, [], [orbit])
    message.submit(
        process_message, [orbit, message, success_criteria, chatbot], [chatbot, orbit]
    )
    success_criteria.submit(
        process_message, [orbit, message, success_criteria, chatbot], [chatbot, orbit]
    )
    go_button.click(
        process_message, [orbit, message, success_criteria, chatbot], [chatbot, orbit]
    )
    reset_button.click(reset, [], [message, success_criteria, chatbot, orbit])
    download_btn.click(export_history, [chatbot], download_btn)

ui.launch(inbrowser=True)
