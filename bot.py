from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ------------------------
# Replace with your BotFather Token
BOT_TOKEN = "7541116150:AAHSiV19V1NqTbPBe6hrG8gapr23aJbbWxQ"
# ------------------------

# In-memory dream journal (for testing; use a database for long-term storage)
dream_journal = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌙 Welcome to the Lucid Dreams Bot!\n\n"
        "Commands:\n"
        "/journal - Write your dream\n"
        "/tips - Get lucid dreaming tips\n"
        "Type /help to see all commands."
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ Available Commands:\n"
        "/start - Welcome message\n"
        "/journal - Save a dream\n"
        "/tips - Learn lucid dreaming techniques"
    )

# /tips command
async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips_list = [
        "🔹 Perform reality checks throughout the day.",
        "🔹 Keep a dream journal every morning.",
        "🔹 Try the MILD (Mnemonic Induction) technique.",
        "🔹 Wake up 5 hours after sleeping, then go back to sleep (WBTB).",
        "🔹 Meditate and visualize your dream before sleeping."
    ]
    tips_text = "\n".join(tips_list)
    await update.message.reply_text(f"💡 Lucid Dreaming Tips:\n\n{tips_text}")

# /journal command
async def journal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Tell me your dream, and I'll save it for you.")
    context.user_data["awaiting_dream"] = True

# Handle dream entries
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

# Run the bot
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("tips", tips))
    app.add_handler(CommandHandler("journal", journal))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_dream))

    print("🤖 Bot is running...")
    await app.run_polling()

from telegram.ext import ApplicationBuilder

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("tips", tips))
app.add_handler(CommandHandler("journal", journal))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_dream))

print("🤖 Bot is running...")
app.run_polling()  # <-- this keeps running indefinitely
