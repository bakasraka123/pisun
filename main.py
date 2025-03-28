from telegram.ext import Application
from dotenv import load_dotenv
import os 

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
app = Application.builder().token(API_TOKEN).build()

app.run_polling(poll_interval=2)