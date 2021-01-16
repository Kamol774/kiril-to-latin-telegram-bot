from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    xabar = "Assalom alaykum, Xush kelibsiz!"
    xabar += "\nKamina <KHALILOV> lotincha so'zni kirilchaga va kirilcha so'zni lotinchaga o'giraman"
    xabar += '\nMatnni kiriting: '
    bot.reply_to(message, xabar)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.polling()




