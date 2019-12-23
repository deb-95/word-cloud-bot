from os import path, getcwd
from telegram import Message
from telegram.ext import CallbackContext
from telegram.update import Update
from utils.settings import Settings
from wordcloud import WordCloud


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

    def save_message(self, update: Update, context: CallbackContext):
        chat_id = str(update.effective_chat.id)
        if chat_id in self.settings.settings["groups"]:
            message: Message = update.message
            with open(f"groups/{chat_id}_messages.txt", "a") as file_to_write:
                file_to_write.write(f"{message.text}\n")

    def make_word_cloud(self, update: Update, context: CallbackContext):
        chat_id = str(update.effective_chat.id)
        if chat_id in self.settings.settings["groups"]:
            directory = path.dirname(__file__) if "__file__" in locals() else getcwd()
            text = open(path.join(directory, f'groups/{chat_id}_messages.txt')).read()
            wc: WordCloud = WordCloud().generate(text)
            context.bot.send_photo(wc.to_image())
