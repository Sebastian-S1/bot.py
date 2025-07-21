import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = "7541116150:AAHSiV19V1NqTbPBe6hrG8gapr23aJbbWxQ"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm alive and running on Render 🚀")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))

    logger.info("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
