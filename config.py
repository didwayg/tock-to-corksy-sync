import os
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
SHEET_ID = os.getenv("SHEET_ID")
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")
