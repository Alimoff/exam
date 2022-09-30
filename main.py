from telegram import (
    Update,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from reverse import reversed_sentence

TOKEN = "5642929511:AAECjK57QPbsldd66ev7FBCURvBr8e3r1U4"


async def start(update: Update, context: ContextTypes):
    """Start the conversation and ask user for input."""
    text = update.message.text
    context.user_data["choice"] = text

    await update.message.reply_text(
        "𝗔𝘀𝘀𝗮𝗹𝗮𝗺𝘂 𝗮𝗹𝗮𝗶𝗸𝘂𝗺!\n"
        "Men kiritgan gapingizni teskarisiga 2 marta yozib berish uchun yasaldim😆\n"
    )

    return True


async def message_handler(update: Update, context: ContextTypes):
    "Handles message entered by the user"

    text = update.message.text
    context.user_data["choice"] = text

    await update.message.reply_text("Success...").sleep(2)

    a = reversed_sentence(text)
    await update.message.reply_text(a)
    await update.message.reply_text(a)

    return True


def main():
    """Run the bot"""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, message_handler))

    application.run_polling()


if __name__ == "__main__":
    main()
