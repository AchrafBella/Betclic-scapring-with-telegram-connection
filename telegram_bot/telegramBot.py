from telegram.ext import Updater, CommandHandler

token = '6976979474:AAEVdRlIttVZqimThh_75dlqW2siCT3H19M'

Bot = Updater(token, use_context=True)
dispatcher = Bot.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello welcome to this bot. Please check help command.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='This bot offre tennis data for the moment using /tennis_match command.')

def tennis_match(update, context):
    # Reading from the file
    with open("output.txt", "r") as file:
        text = file.read()

    for elm in text.split('|'):
        context.bot.send_message(chat_id=update.effective_chat.id, text=elm)


tennis_handler = CommandHandler('tennis_match', tennis_match)
start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', start)

dispatcher.add_handler(tennis_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)

Bot.start_polling()
Bot.idle()
