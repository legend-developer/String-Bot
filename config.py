from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","25028796"))
API_HASH = getenv("API_HASH","885615da36b5b0128f86159f77a20a0e")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))

MONGO_DB_URI = ("MONGO_DB_URI","mongodb+srv://shiv230708:shivam@23@cluster0.0awjqhr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "https://t.me/life_changing_movies")
