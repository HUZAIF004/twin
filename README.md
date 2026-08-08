# Digital Twin

This project contains a Gradio-based AI Digital Twin. It provides an interactive chat interface allowing users to converse with an AI persona that represents your professional background, skills, and experience.

## Features

- **Interactive Chat Interface**: A sleek, dark-themed UI built with Gradio.
- **AI Persona**: Uses OpenRouter's API to power the conversational AI twin.
- **Tool Integration**: The AI has access to custom tools (defined in `tools.py`) to provide detailed responses based on your `resume.pdf` and `summary.txt`.

## Prerequisites

Before running the application, make sure you have:

1. **Python**: Python 3.8 or higher installed on your system.
2. **API Keys**: You will need an OpenRouter API key to power the AI.
3. **Environment Variables**: Create a `.env` file in this directory with your credentials:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   
   # Optional: For notifications, if you have Pushover tools configured
   PUSHOVER_USER=your_pushover_user_key
   PUSHOVER_TOKEN=your_pushover_app_token
   ```

## Setup & Installation

1. Open a terminal in this `twin` directory.
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the App Locally

To start the Digital Twin locally, run:

```bash
python app.py
```

This will launch the Gradio server. It will provide a local URL (e.g., `http://127.0.0.1:7860/`) which you can open in your browser to interact with your twin.

## Deployment

You can deploy this application for free on [Render](https://render.com/). 

For complete step-by-step instructions on deploying your twin to the web, please see the `RENDER_INSTRUCTIONS.md` file located in the parent directory (`1_foundations/RENDER_INSTRUCTIONS.md`).

## Customization

- **Resume & Summary**: Replace `resume.pdf` and `summary.txt` with your own documents to personalize the AI's knowledge.
- **Styling**: The aesthetic look of the app (colors, fonts, glassmorphism) can be customized within `styles.py`.
- **System Prompt**: Adjust the AI's personality and instructions within `context.py`.
