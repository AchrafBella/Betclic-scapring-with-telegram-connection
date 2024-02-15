from telegram.ext import Updater, CommandHandler
from Betclic_tennis_scraper import get_tennis_matches
token = '6820009462:AAFRd8TiKYNFoLpbsMW0Tb_S0J5iP8KqvNw'

Bot = Updater(token, use_context=True)
dispatcher = Bot.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello welcome to this bot. Please check help command.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='This bot offre tennis data & baskket ball data using /tennis_match & /basket_match command.')

def tennis_match(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please wait till we get the matchs.')
    get_tennis_matches(update, context)
    
def basket_match(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Comming soon.')

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
tennis_handler = CommandHandler('tennis_match', tennis_match)
basket_handler = CommandHandler('basket_match', basket_match)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(tennis_handler)
dispatcher.add_handler(basket_handler)

Bot.start_polling()
Bot.idle()
