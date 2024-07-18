import gradio as gr

def generate_response(prompt):
    return "You entered: " + prompt

def home_page():
    return "Welcome to the Prompt Generator! Enter your prompt below:"

iface = gr.Interface(
    fn=generate_response, 
    inputs=gr.inputs.Textbox(label="Enter your prompt"), 
    outputs="text",
    title="Prompt Generator",
    description="Generate a response based on the given prompt.",
    examples=[["What's your favorite color?"]]
)
iface.launch(share=True, debug=True, home_page=home_page)