from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
ONTOP_URL = os.getenv("ONTOP_URL")
