from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import environ
TOKEN = '598184545:AAESpk_Ji0JgG_zQsw3g1cvtkTf7k-5vbdA'
my_chat_id = '@wmesh_channel'
updater = Updater(TOKEN) # Токен API к Telegram
dispatcher = updater.dispatcher
# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)
    print(update.message.chat_id)
    # bot.send_message(chat_id=my_chat_id, text=response)
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

# import requests
# import datetime
# import time
#
# class BotHandler:
#
#     def __init__(self, token):
#         self.token = token
#         self.api_url = "https://api.telegram.org/bot{}/".format(token)
#         print(self.api_url)
#
#     def get_updates(self, offset=None, timeout=30):
#         method = 'getUpdates'
#         params = {'timeout': timeout, 'offset': offset}
#         resp = requests.get(self.api_url + method, params)
#         result_json = resp.json()['result']
#         return result_json
#
#     def send_message(self, chat_id, text):
#         params = {'chat_id': chat_id, 'text': text}
#         method = 'sendMessage'
#         resp = requests.post(self.api_url + method, params)
#         print(self.api_url + method)
#         return resp
#
#     def get_last_update(self):
#         get_result = self.get_updates()
#
#         if len(get_result) > 0:
#             last_update = get_result[-1]
#         else:
#             last_update = get_result[len(get_result)]
#
#         return last_update
#
# greet_bot = BotHandler('598184545:AAESpk_Ji0JgG_zQsw3g1cvtkTf7k-5vbdA')
# greetings = ('здравствуй', 'привет', 'ку', 'здорово')
# now = datetime.datetime.now()
#
# def main():
#     new_offset = None
#     today = now.day
#     hour = now.hour
#
#     while True:
#         time.sleep(1)
#         print("Hello")
#         greet_bot.send_message(1, 'Доброе утро, {}')
#
#
#         # last_update = greet_bot.get_last_update()
#         #
#         # last_update_id = last_update['update_id']
#         # last_chat_text = last_update['message']['text']
#         # last_chat_id = last_update['message']['chat']['id']
#         # last_chat_name = last_update['message']['chat']['first_name']
#         #
#         # if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
#         #     greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
#         #     today += 1
#         #
#         # elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
#         #     greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
#         #     today += 1
#         #
#         # elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
#         #     greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
#         #     today += 1
#         #
#         # new_offset = last_update_id + 1
#
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         exit()
