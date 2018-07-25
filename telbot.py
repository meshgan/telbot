from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import environ
TOKEN = '598184545:AAESpk_Ji0JgG_zQsw3g1cvtkTf7k-5vbdA'
my_chat_id = '@mesh_channel'
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
counter = int(0)  # type: int
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello! Please send us your email.')
def textMessage(bot, update):
    answer = update.message.text
    global counter
    if counter == 0:
        if "&" and "." in answer:
            response = "Please send us your ERC20 wallet."
            counter += 1
        else:
            response = "There is a mistake. Please send us your email."

    else:
        if counter == 1:
            if "0x" in answer:
                response = 'Please send us your passport photo '
                counter = counter + 1
            else:
                response = "There is a mistake. Please send us your ERC20 wallet."

    bot.send_message(chat_id=update.message.chat_id, text=response)
# Хендлеры
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
PORT = int(environ.get('PORT', '5000'))
updater.start_webhook(listen="0.0.0.0",
                    port=PORT,
                    url_path=TOKEN)
updater.bot.setWebhook("https://obscure-wildwood-96925.herokuapp.com/" + TOKEN)
#updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
