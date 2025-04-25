from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os 

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
   await update.message.reply_text("Hi")

app = Application.builder().token(API_TOKEN).build()

app.add_handler(CommandHandler("start", start_command))

print("all good")

app.run_polling(poll_interval=2)