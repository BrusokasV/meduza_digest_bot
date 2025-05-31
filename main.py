import os
from typing import Final
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Hello, {update.effective_user.first_name}. I am {BOT_USERNAME}. If you would like me to forward you the daily news digest from t.me/meduzalive, use /subscribe."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I was created to forward you the daily news digest from t.me/meduzalive. I was created for convenience, and my creator has no affiliation with the news agency. Use /subscribe to start receiving updates or /unsubscribe to stop receiving them."
    )

async def subscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(
    #     "You have subscribed to the daily news digest."
    # )
    await update.message.reply_text(
        "You have elected to subscribe. The feature is not yet implemented."
    )
    #Implementation

async def unsubscribe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await update.message.reply_text(
    #     "You have unsubscribed from the daily news digest."
    # )
    await update.message.reply_text(
        "You have elected to unsubscribe. The feature is not yet implemented."
    )
    #Implementation

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private':
        await update.message.reply_text(
            "Please use commands like /start, /help, /subscribe, or /unsubscribe to interact with me."
        )

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    await update.message.reply_text("An error occurred. Please try again later.")

if __name__ == "__main__":
    print("Starting the app...")
    app = Application.builder().token(TOKEN).build()

    # Command Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("subscribe", subscribe_command))
    app.add_handler(CommandHandler("unsubscribe", unsubscribe_command))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error Handler
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)