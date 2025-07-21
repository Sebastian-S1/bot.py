import telegram
print("✅ Version:", telegram.__version__)

from telegram import ApplicationBuilder 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7541116150:AAHSiV19V1NqTbPBe6hrG8gapr23aJbbWxQ"  # Replace with your bot token

async def start(update: ApplicationBuilder, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is working on Render!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    
    # Start the bot
    app.run_polling()

if __name__ == "__main__":
    main()
