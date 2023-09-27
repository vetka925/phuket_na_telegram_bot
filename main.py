import os
import logging

from telegram import  Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes
)

from keyboards import KEYBOARDS, start_keyboard, start_admin_keyboard
# from answers import ANSWERS, START_MESSAGE
from admin_handler import get_admin_handler
from database import NABotDB

from dotenv import load_dotenv


db = NABotDB(db_path='bot.db')

CALLBACK_NAMES = {
    '/about',
    '/schedule',
    '/anonymous',
    '/whoismember',
    '/whatisna',
    '/whatismeeting',
    '/firsttime',
    '/weweb',
    '/main',
    '/addicted',
    '/rules',
    '/phuket',
    '/history'
    }


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    await update.message.reply_text(db.get_text_by_name('main'), 
                                    reply_markup=start_keyboard, parse_mode='HTML')

def build_callback_handler(callback_data):
    async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Show new choice of buttons"""
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=db.get_text_by_name(callback_data[1:]), reply_markup=KEYBOARDS[callback_data], parse_mode='HTML'
        )
    return callback_handler


conv_handler = get_admin_handler(db, CALLBACK_NAMES)

def main() -> None:
    """Run the bot."""
    load_dotenv()
    application = Application.builder().token(os.environ['TOKEN']).build()
    application.add_handler(CommandHandler("start", start))
    for callback in CALLBACK_NAMES:
        handler = CallbackQueryHandler(build_callback_handler(callback), pattern=callback)
        application.add_handler(handler)
    application.add_handler(conv_handler)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()