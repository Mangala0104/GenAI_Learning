import os 
from dotenv import load_dotenv,dotenv_values,find_dotenv

#loads  .env from current directory 
load_dotenv()

config = dotenv.values(".env")
api_key = config.get("GEMINI_API_KEY")
api_key = os.getenv("GEMINI_API_KEY","")
api_key = os.environt["GEMINI_API_KEY"]
