import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from database import NABotDB

def get_admin_handler( db: NABotDB, CALLBACK_NAMES: str):
    CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

    reply_keyboard = [[e[1:]] for e in CALLBACK_NAMES] + [['✅ FINISH']]
    reply_keyboard_regexp = f"^({'|'.join([e[1:] for e in CALLBACK_NAMES])})$"
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Start the conversation and ask user for input."""
        if str(update.message.from_user.id) in db.get_admins():
            await update.message.reply_text(
                "Choose what message you want to update",
                reply_markup=markup,
            )

            return CHOOSING

    async def regular_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Ask the user for info about the selected predefined choice."""
        text = update.message.text
        context.user_data["choice"] = text
        print(text)
        await update.message.reply_text(f"**Current text:**\n\n\n{db.get_text_by_name(text)}\n\n\n**Enter new text...**")

        return TYPING_REPLY

    async def received_information(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Store info provided by user and ask for the next category."""
        user_data = context.user_data
        text = update.message.text
        name = user_data["choice"]
        del user_data["choice"]
        db.edit_row(name=name, new_text=text)
        await update.message.reply_text(
            f"You just updated '{name}' message! You can choose another message to update",
            reply_markup=markup,
        )

        return CHOOSING


    async def done(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        """Display the gathered info and end the conversation."""
        user_data = context.user_data
        if "choice" in user_data:
            del user_data["choice"]

        await update.message.reply_text(
            f"Done! Until next time!",
            reply_markup=ReplyKeyboardRemove(),
        )

        user_data.clear()
        return ConversationHandler.END

    return ConversationHandler(
            entry_points=[CommandHandler("admin", start)],
            states={
                CHOOSING: [
                    MessageHandler(
                        filters.Regex(reply_keyboard_regexp), regular_choice
                    )            ],
                TYPING_CHOICE: [
                    MessageHandler(
                        filters.TEXT & ~(filters.COMMAND | filters.Regex("^✅ FINISH$")), regular_choice
                    )
                ],
                TYPING_REPLY: [
                    MessageHandler(
                        filters.TEXT & ~(filters.COMMAND | filters.Regex("^✅ FINISH$")),
                        received_information,
                    )
                ],
            },
            fallbacks=[MessageHandler(filters.Regex("^✅ FINISH$"), done)],
        )