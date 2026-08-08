from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv, find_dotenv
import gradio as gr
import os

load_dotenv(find_dotenv(), override=True)
openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
openrouter = OpenAI(api_key=openrouter_api_key, base_url=OPENROUTER_BASE_URL)
MODEL_NAME = "openrouter/free"


system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system.copy()
    
    # Add history messages from Gradio's default tuple format [[user_msg, bot_msg], ...]
    for user_msg, bot_msg in history:
        if user_msg:
            messages.append({"role": "user", "content": user_msg})
        if bot_msg:
            messages.append({"role": "assistant", "content": bot_msg})
            
    messages.append({"role": "user", "content": message})
    
    response = openrouter.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response and response.choices and response.choices[0].finish_reason == "tool_calls":
        msg = response.choices[0].message
        tool_calls = msg.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(msg)
        messages.extend(results)
        response = openrouter.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
        
    if response and response.choices:
        return response.choices[0].message.content
    return "Error: No response received from model."


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Digital Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False, elem_classes="chatbot"),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base(),inbrowser=True)
