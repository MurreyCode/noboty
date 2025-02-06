README
======

# Telegram AI Chatbot

This project is a **Telegram bot** powered by a **small AI model** (e.g., `microsoft/phi-2`) to generate responses based on user inputs. The bot leverages **Hugging Face's transformers library** and runs on **PyTorch**.

## Features
- 🚀 AI-powered chatbot using `transformers`
- 🤖 Handles text-based user interactions
- 🔄 Generates dynamic responses
- 📡 Runs on Telegram via `python-telegram-bot`

## Installation

Ensure you have **Python 3.8+** installed. Then, install dependencies:

    pip install transformers torch python-telegram-bot

Alternatively, if using **Poetry**:

    poetry install

## Setup
1. Create a bot on Telegram using [BotFather](https://t.me/BotFather)
2. Obtain your **Telegram bot token**
3. Add the token to the script (`TOKEN = "your-bot-token"`)

## Running the Bot

Run the bot locally:

    poetry run python src/main.py

Or using Python directly:

    python src/main.py

## Configuration
Modify the AI model in `main.py`:

    MODEL_NAME = "microsoft/phi-2"

You can replace it with another small model like:

    "mistralai/Mistral-7B-Instruct"
    "tiiuae/falcon-7b-instruct"

## Usage
Start a conversation by sending `/start` to the bot.
Send any message, and the bot will reply with an AI-generated response.

## License
This project is licensed under the **MIT License**. See `LICENSE` for details.

## Contributing
Feel free to submit issues and pull requests. Contributions are welcome!

## Acknowledgments
- 🤗 Hugging Face for `transformers`
- 🚀 Open-source AI models
- 🔥 Python & PyTorch community
