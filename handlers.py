from telegram.ext import CallbackContext
from telegram.update import Update
from utils.settings import Settings


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def get_user_id(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    context.bot.send_message(chat_id=chat_id, text=f"Here is your ID: {user_id}")


class HandlersContainer:
    settings: Settings = None

    def __init__(self, settings):
        self.settings = settings

    def add_chat_to_allowed(self, update: Update, context: CallbackContext):
        chat_id = str(update.effective_chat.id)
        user_id = str(update.effective_user.id)
        if user_id in self.settings.settings["admins"]:
            self.settings.add_to_list("groups", chat_id)
            context.bot.send_message(chat_id=chat_id, text=f"Done.")
        else:
            context.bot.send_message(chat_id=chat_id, text=f"You are not allowed.")
