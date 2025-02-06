from telethon.sync import TelegramClient

SESSION_FILE = "my_session"
API_ID = ""
API_HASH = ""
CHANNEL_USERNAME = "@nowhereNUDES"

if __name__ == "__main__":
    with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        for message in client.iter_messages(CHANNEL_USERNAME, limit=100):
            print(message.text)
