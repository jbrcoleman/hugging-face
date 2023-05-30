from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

# Create the Gradio interface
demo = gr.Interface(fn=predict, 
                     inputs="text", 
                     outputs="text", 
                     title="Text Summarization", 
                     description="Enter some text and get a summary of it.")

demo.launch()