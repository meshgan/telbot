from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from os import environ
TOKEN = '598184545:AAESpk_Ji0JgG_zQsw3g1cvtkTf7k-5vbdA'
my_chat_id = '@mesh_channel'
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
#counter = int(0)  # type: int

MAIL, WALLET, PHOTO = range(3)

# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello! Please send us your email.')
    return MAIL

def mailMessage(bot, update):
    if "&" and "." in update.message.text:
        response = "Please send us your ERC20 wallet."
        bot.send_message(chat_id=update.message.chat_id, text=response)
        return WALLET
    else:
        response = "There is a mistake. Please send us your email."
        bot.send_message(chat_id=update.message.chat_id, text=response)
        return MAIL

def walletMessage(bot, update):
    if "0x" in update.message.text:
        response = "Please send us your passport photo."
        bot.send_message(chat_id=update.message.chat_id, text=response)
        return PHOTO
    else:
        response = "There is a mistake. Please send us your ERC20 wallet."
        bot.send_message(chat_id=update.message.chat_id, text=response)
        return WALLET

def photoMessage(bot, update):
    user = update.message.from_user
    photo_file = bot.get_file(update.message.photo[-1].file_id)
    photo_file.download('user_photo.jpg')
    bot.send_message(chat_id=update.message.chat_id, text="Thank you")

def cancel(bot, update):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.')
    return ConversationHandler.END



# def textMessage(bot, update):
#     answer = update.message.text
#     global counter
#     if counter == 0:
#         if "&" and "." in answer:
#             response = "Please send us your ERC20 wallet."
#             counter += 1
#         else:
#             response = "There is a mistake. Please send us your email."
#
#         return WALLET
#
#     elif counter == 1:
#         if "0x" in answer:
#             response = 'Please send us your passport photo '
#             counter = counter + 1
#         else:
#             response = "There is a mistake. Please send us your ERC20 wallet."
#
#         return PHOTO
#
#     bot.send_message(chat_id=update.message.chat_id, text=response)


# Хендлеры
#start_command_handler = CommandHandler('start', startCommand)
#text_message_handler = MessageHandler(Filters.text, textMessage)
#photo_message_handler = MessageHandler(Filters.photo, photoMessage)

# Добавляем хендлеры в диспетчер
conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', startCommand)],

        states={
            MAIL: [MessageHandler(Filters.text, mailMessage)],
            WALLET: [MessageHandler(Filters.text, walletMessage)],
            PHOTO: [MessageHandler(Filters.photo, photoMessage)],
        },

         fallbacks=[CommandHandler('cancel', cancel)]
    )

dispatcher.add_handler(conv_handler)

# dispatcher.add_handler(start_command_handler)
# dispatcher.add_handler(text_message_handler)
# dispatcher.add_handler(photo_message_handler)


# Начинаем поиск обновлений
PORT = int(environ.get('PORT', '5000'))
updater.start_webhook(listen="0.0.0.0",
                    port=PORT,
                    url_path=TOKEN)
updater.bot.setWebhook("https://obscure-wildwood-96925.herokuapp.com/" + TOKEN)
updater.start_polling()
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
