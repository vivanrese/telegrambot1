KEY = '1692606694:AAFTcwiIB-9O0crKmvlw5iEay7k94LNhpFs'
from telegram.ext import *
from nsetools import Nse
nse = Nse()
print("Bot started")


def start_command(update, context):
    update.message.reply_text(
        'Hello friend, be sure to check ** /commands **. Send stock ID')


def help_command(update, context):
    update.message.reply_text('I cannot help you. Contact admin')


def rules_command(update, context):
    update.message.reply_text('/topGainers -> Top Gainers \n/topLosers -> Top Losers \n')

def get_lot_size_command(update, context):
    temp = nse.get_fno_lot_sizes()
    ans = ''
    for i,j in temp.items():
        ans += i+': '+j+'\n'
    update.message.reply_text(ans)

def top_gainers_command(update, context):
    top = nse.get_top_gainers()
    for t in top:
        update.message.reply_text('Stock: '+t['symbol']+'\n'+'Open Price: '+str(t['openPrice'])+'\n'+'High Price: '+str(t['highPrice'])+'\n'+'Low Price: '+str(t['highPrice'])+'\n')

def top_losers_command(update, context):
    top = nse.get_top_losers()
    for t in top:
        update.message.reply_text('Stock: '+t['symbol']+'\n'+'Open Price: '+str(t['openPrice'])+'\n'+'High Price: '+str(t['highPrice'])+'\n'+'Low Price: '+str(t['highPrice'])+'\n')

def handle_message(update, context):
    q = update.message.text.upper()
    if q in nse.get_stock_codes():
        ans = nse.get_quote(q)
        ret = 'Average Price: ' + str(
            ans['averagePrice']) + '\n' + 'Close Price: ' + str(
                ans['closePrice']
            ) + '\n' + 'Company Name: ' + ans['companyName'] + '\n'
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
    dp.add_handler(CommandHandler("commands", rules_command))
    dp.add_handler(CommandHandler("topGainers", top_gainers_command))
    dp.add_handler(CommandHandler("topLosers", top_losers_command))
    dp.add_handler(CommandHandler("getLotSize", get_lot_size_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    up.start_polling()
    up.idle()


main()
