from lib2to3.pgen2.token import STAR
import logging

from telegram import __version__ as TG_VER
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

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

from reverse import reversed_sentence

START, MESSAGE, HANDLER = range(3)

TOKEN = "5642929511:AAECjK57QPbsldd66ev7FBCURvBr8e3r1U4"


async def start(update: Update, context: ContextTypes):
    """Start the conversation and ask user for input."""
    text = update.message.text
    context.user_data["choice"] = text

    await update.message.reply_text(
        "𝗔𝘀𝘀𝗮𝗹𝗮𝗺𝘂 𝗮𝗹𝗮𝗶𝗸𝘂𝗺!\n"
        "Men kiritgan gapingizni teskarisiga 2 marta yozib berish uchun yasaldim😆\n"
    )

    return START


async def message(update: Update, context: ContextTypes):
    """Handles message"""

    await update.message.reply_text("So'z yoki gap kiriting: ")

    return MESSAGE


async def message_handler(update: Update, context: ContextTypes):
    "Handles message entered by the user"

    text = update.message.text
    context.user_data["choice"] = text

    await update.message.reply_text("Success...")

    a = reversed_sentence(text)
    await update.message.reply_text(a)
    await update.message.reply_text(a)

    return HANDLER


def main():
    """Run the bot"""
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START: [MessageHandler(filters.TEXT, message_handler)],
            # MESSAGE: [MessageHandler(filters.TEXT, message_handler)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
