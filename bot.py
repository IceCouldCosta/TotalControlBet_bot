import telebot
from config import TOKEN, CHANNEL_ID, ADMIN_ID
import datetime

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать! Бот активен 🔥")

@bot.message_handler(commands=['статус'])
def status(message):
    bot.send_message(message.chat.id, f"✅ Бот работает\n⏰ Время сервера: {datetime.datetime.now()}")

def post_prediction():
    text = "🎯 Прогноз на матч\nФутбол ⚽️\nChelsea vs Flamengo\nСтавка: П1\nКоэффициент: 1.85"
    bot.send_message(CHANNEL_ID, text)

def notify_admin(text):
    bot.send_message(ADMIN_ID, text)

if __name__ == '__main__':
    notify_admin("Бот запущен ✅")
    post_prediction()
    bot.polling(none_stop=True)
