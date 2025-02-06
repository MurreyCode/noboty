import os
import dotenv
from telethon.sync import TelegramClient

dotenv.load_dotenv()

SESSION_FILE = "my_session"
API_ID = os.getenv("API_ID")  # Get from environment
API_HASH = os.getenv("API_HASH")  # Get from environment
CHANNEL_USERNAME = "@nowhereNUDES"

if __name__ == "__main__":
    with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        for message in client.iter_messages(CHANNEL_USERNAME, limit=100):
            print(message.text)
