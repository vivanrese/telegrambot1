KEY = '1692606694:AAFTcwiIB-9O0crKmvlw5iEay7k94LNhpFs'
from telegram.ext import *
from nsetools import Nse
print("Bot started")

def start_command(update, context):
  update.message.reply_text('Hello friend, be sure to check /rules. Send stock ID')

def help_command(update, context):
  update.message.reply_text('I cannot help you. Contact admin')

def rules_command(update, context):
  update.message.reply_text('Custom command check. Send stock ID')

def handle_message(update, context):
  q = update.message.text.upper()
  nse = Nse()
  if q in nse.get_stock_codes():
    ans = nse.get_quote(q)
    ret = 'Average Price: '+str(ans['averagePrice'])+'\n'+'Close Price: '+str(ans['closePrice'])+'\n'+'Company Name: '+ans['companyName']+'\n'
    update.message.reply_text(ret)
  else:
    update.message.reply_text('Invalid Stock')
def error(update, context):
  print(f'Update {update} caused err {context.error}')

def main():
  up = Updater(KEY, use_context=True)
  dp = up.dispatcher

  dp.add_handler(CommandHandler("start", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("rules", rules_command))
  dp.add_handler(MessageHandler(Filters.text, handle_message))

  dp.add_error_handler(error)
  up.start_polling()
  up.idle()

main()
    

