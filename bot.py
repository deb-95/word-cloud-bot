import logging

from telegram.ext import Updater, Filters, CommandHandler, MessageHandler
from handlers import start, get_user_id, HandlersContainer
from utils.settings import Settings


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    settings_obj = Settings()
    updater = Updater(token=settings_obj.settings["token"], use_context=True)
    handlers_obj = HandlersContainer(settings_obj)
    set_handlers(handlers_obj, updater)
    updater.start_polling()


def set_handlers(handlers_obj: HandlersContainer, updater: Updater):
    start_handler = CommandHandler('start', start)
    user_id_handler = CommandHandler('userid', get_user_id)
    add_group_handler = CommandHandler('addgroup', handlers_obj.add_chat_to_allowed)
    word_cloud_handler = CommandHandler('generatewc', handlers_obj.make_word_cloud)
    message_handler = MessageHandler(Filters.text, handlers_obj.save_message)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(user_id_handler)
    dispatcher.add_handler(add_group_handler)
    dispatcher.add_handler(word_cloud_handler)


if __name__ == '__main__':
    main()
