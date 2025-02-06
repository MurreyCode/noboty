import logging
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)

logging.basicConfig(level="INFO")

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
TOKEN = "8036979597:AAHnS3TCK2A6YcYe6I6q8HnKpsGd0uFxGWE"

# Load deepseek model and tokenizer (small model for efficiency)
# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
MODEL_NAME = "microsoft/phi-2"

logging.info("Loading tokeniser")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
logging.info("Loading model")
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32, device_map="auto")

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! I'm an AI-powered bot. How can I assist you?")

async def generate_response(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    await update.message.reply_text("Thinking... 🤖")

    # Tokenize input and generate response
    logging.info(f"Tokenising the user input: {user_input}")
    inputs = tokenizer(
        user_input, 
        return_tensors="pt", 
        padding=True, 
        truncation=True,
        )
    input_ids = inputs.input_ids.to(model.device)
    attention_mask = inputs.attention_mask.to(model.device)    
    logging.info(f"{len(inputs)} input tokens generated")

    with torch.no_grad():
        logging.info("Generating answer tokens")
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,  # Pass attention mask
            max_length=20,
            pad_token_id=tokenizer.eos_token_id  # Explicitly set pad token
        )        
        logging.info(f"{len(output)} answer tokend generated")

    logging.info("Decoding answer")
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    logging.info(f"Returning answer: {response}")
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_response))

    logging.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
