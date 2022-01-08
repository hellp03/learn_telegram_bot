import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from telegram.ext.callbackcontext import CallbackContext

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log',encoding='utf8')

def greet_user(update, context: CallbackContext):
    text='Ну здравствуй'
    print(text)
    update.message.reply_text('Ну здравствуй!')
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="I'm a bot, please talk to me!")

def talk_to_me(update, context: CallbackContext):
    user_text=update.message.text
    print('{}, ты пишешь {}, но ты делаешь это без уважения!'.format(update.message.chat.username,update.message.text))
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, update.message.chat.id,
                    update.message.text)
    update.message.reply_text('{}, ты пишешь мне{}, но ты делаешь это без уважения!'.format(update.message.chat.username,update.message.text))

def main():
    mybot = Updater(settings.API_KEY)
    logging.info('Bot start, Русский')
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
    

main()