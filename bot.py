from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ✅ Your Bot Token
BOT_TOKEN = "7541116150:AAHSiV19V1NqTbPBe6hrG8gapr23aJbbWxQ"

dream_journal = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌙 Welcome to the Lucid Dreams Bot!\n\n"
        "Commands:\n"
        "/journal - Write your dream\n"
        "/tips - Get lucid dreaming tips\n"
        "/help - Show all commands"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ Available Commands:\n"
        "/start - Welcome message\n"
        "/journal - Save a dream\n"
        "/tips - Lucid dreaming techniques"
    )

async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips_list = [
        "🔹 Perform reality checks throughout the day.",
        "🔹 Keep a dream journal every morning.",
        "🔹 Try the MILD technique.",
        "🔹 Wake up after 5 hours, then go back to sleep (WBTB).",
        "🔹 Meditate and visualize your dream before sleeping."
    ]
    await update.message.reply_text("💡 Lucid Dreaming Tips:\n\n" + "\n".join(tips_list))

async def journal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Tell me your dream, and I'll save it for you.")
    context.user_data["awaiting_dream"] = True

async def save_dream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get("awaiting_dream"):
        user_id = update.effective_user.id
        dream_text = update.message.text

        if user_id not in dream_journal:
            dream_journal[user_id] = []
        dream_journal[user_id].append(dream_text)

        await update.message.reply_text("✅ Your dream has been saved!")
        context.user_data["awaiting_dream"] = False
    else:
        await update.message.reply_text("❗Use /journal before sending a dream.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("journal", journal))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_dream))

    print("🤖 Bot is running...")
    app.run_polling()
