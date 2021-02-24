import requests
import json
import telebot


def getvalue(h):
    r = requests.get('https://blockchain.info/ru/ticker')
    a = json.loads(r.text)
    d = a[h]
    return d


bot = telebot.TeleBot('1610772384:AAEKcwh_FduWgCARlhc5Rk_j1nvFcCsuNM4')


@bot.message_handler(content_types=['text'])
def text(message):
    r = getvalue(message.text)
    bot.send_message(message.chat.id, f'last:{r["last"]}')
    bot.send_message(message.chat.id, f'buy:{r["buy"]}')
    bot.send_message(message.chat.id, f'sell:{r["sell"]}')

bot.polling()
