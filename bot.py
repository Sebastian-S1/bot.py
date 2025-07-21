import telegram
print("✅ Version:", telegram.__version__)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your actual token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is now running on Render!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add your command handlers
    app.add_handler(CommandHandler("start", start))
    
    # Start the bot (replaces Updater.start_polling())
    app.run_polling()

if __name__ == "__main__":
    main()
