import os

from dotenv import load_dotenv

load_dotenv(override=True)

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVERS_EMAIL = os.getenv("RECEIVERS_EMAIL")
