import gradio as gr
import requests
import os

# API endpoint URL (configurable via environment variable)
API_URL = os.getenv("API_URL", "http://localhost:8000")

def text_similarity_check(first_text: str, second_text: str) -> str:
    """Interface for task1"""
    try:
        response = requests.post(
            f"{API_URL}/task1",
            json={
                "first_text": first_text.strip(),
                "second_text": second_text.strip(),
            }
        )
        result = response.json()
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def process_instructions(template: str, input_text: str) -> str:
    """Interface for task2"""
    try:
        response = requests.post(
            f"{API_URL}/task2",
            json={
                "template": template,
                "input_text": input_text
            }
        )
        result = response.json()
        return f"Result: {result['result']}\n\nExplanation: {result['explanation']}"
    except Exception as e:
        return f"Error: {str(e)}"

def implement_feedback(text: str, target: str, instruction: str) -> str:
    """Interface for task3"""
    try:
        response = requests.post(
            f"{API_URL}/task3",
            json={
                "text": text,
                "target": target,
                "instruction": instruction
            }
        )
        result = response.json()
        return f"Updated Text: {result['updated_text']}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="NLP Tasks Interface") as demo:
    gr.Markdown("# NLP Tasks Interface")
    
    with gr.Tab("Text Similarity"):
        with gr.Column():
            text1_input = gr.Textbox(label="First Text", lines=3)
            text2_input = gr.Textbox(label="Second Text", lines=3)
            similarity_button = gr.Button("Check Similarity")
            similarity_output = gr.Textbox(label="Result", lines=5)
            
            similarity_button.click(
                text_similarity_check,
                inputs=[text1_input, text2_input],
                outputs=similarity_output
            )
    
    with gr.Tab("Instruction Processing"):
        with gr.Column():
            template_input = gr.Textbox(label="Template", lines=3)
            instruction_input = gr.Textbox(label="Input Text", lines=3)
            process_button = gr.Button("Process Text")
            process_output = gr.Textbox(label="Result", lines=5)
            
            process_button.click(
                process_instructions,
                inputs=[template_input, instruction_input],
                outputs=process_output
            )
    
    with gr.Tab("Feedback Implementation"):
        with gr.Column():
            text_input = gr.Textbox(label="Text", lines=3)
            target_input = gr.Textbox(label="Target", lines=2)
            feedback_input = gr.Textbox(label="Instruction", lines=2)
            feedback_button = gr.Button("Implement Feedback")
            feedback_output = gr.Textbox(label="Result", lines=5)
            
            feedback_button.click(
                implement_feedback,
                inputs=[text_input, target_input, feedback_input],
                outputs=feedback_output
            )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",  # Allow external connections
        server_port=7860,
        share=True  # Generate a public URL that can be shared
    ) 