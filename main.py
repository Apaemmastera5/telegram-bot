import os
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TOKEN")  # зчитує токен із Render Environment Variables

async def start(update, context):
    await update.message.reply_text("Привіт! Я працюю 🚀")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
