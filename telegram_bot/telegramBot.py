from telegram.ext import Updater, CommandHandler
from Betclic_tennis_scraper import get_tennis_matches
token = '6976979474:AAEVdRlIttVZqimThh_75dlqW2siCT3H19M'

Bot = Updater(token, use_context=True)
dispatcher = Bot.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello welcome to this bot. Please check help command.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='This bot offre tennis data for the moment using /tennis_match command.')

def tennis_match(update, context):
    all_matches_text = get_tennis_matches()
    
    for elm in all_matches_text:
        context.bot.send_message(chat_id=update.effective_chat.id, text=elm)

start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
tennis_handler = CommandHandler('tennis_match', tennis_match)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(tennis_handler)

Bot.start_polling()
Bot.idle()
