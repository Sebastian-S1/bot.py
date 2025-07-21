import telegram
print("✅ Version:", telegram.__version__)

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# ✅ Define a command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! ✅ Your bot is running successfully!")

# ✅ Main function
def main():
    # Build application (replaces old Updater)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))

    logger.info("🚀 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
