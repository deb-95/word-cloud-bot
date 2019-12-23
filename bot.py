import logging
import json

from telegram.ext import Updater
from telegram.ext import CommandHandler
from handlers import start, get_user_id, HandlersContainer
from utils.settings import Settings
from wordcloud import WordCloud


def main():
    settings_obj = Settings()
    updater = Updater(token=settings_obj.settings["token"], use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    handlers_obj = HandlersContainer(settings_obj)
    start_handler = CommandHandler('start', start)
    message_handler = CommandHandler('start', start)
    user_id_handler = CommandHandler('userid', get_user_id)
    add_group_handler = CommandHandler('addgroup', handlers_obj.add_chat_to_allowed)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(user_id_handler)
    dispatcher.add_handler(add_group_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()
