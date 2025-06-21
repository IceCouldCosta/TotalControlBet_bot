import telebot
import datetime
import threading
import time
from config import TOKEN, CHANNEL_ID, ADMIN_ID

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

# Команды
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Привет! Бот готов публиковать прогнозы и итоги.")

@bot.message_handler(commands=['статус'])
def status(message):
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    bot.send_message(message.chat.id, f"✅ Бот активен\n⏰ Время сервера: {now}")

# ===== ПУБЛИКАЦИИ =====
def post_morning_prediction():
    text = (
        "🎯 <b>Утренняя ставка</b>\n\n"
        "⚽️ <b>Матч:</b> Chelsea vs Flamengo\n"
        "📌 <b>Прогноз:</b> Победа Flamengo\n"
        "💸 <b>Коэффициент:</b> 2.35\n"
        "🔗 <a href='https://leadgid.link'>Ставка по партнёрской ссылке</a>\n\n"
        "<i>Голос комментатора:</i> «Total Control — прогнозы, которые кричат!»"
    )
    bot.send_message(CHANNEL_ID, text)

def post_reaction():
    text = (
        "🎙 <b>Событие в матче!</b>\n\n"
        "⚽️ Гол! Flamengo забивает!\n"
        "🔥 Комментатор: «ДААА! Вот это удар! Вот это контроль!»"
    )
    bot.send_message(CHANNEL_ID, text)

def post_summary():
    text = (
        "📊 <b>Итоги дня</b>\n\n"
        "🧮 Прогнозов: 2\n"
        "✅ Зашли: 1\n"
        "❌ Не зашли: 1\n"
        "💰 ROI: +12%\n\n"
        "🔗 <a href='https://leadgid.link'>Сделать ставку с нами</a>"
    )
    bot.send_message(CHANNEL_ID, text)

# ===== РАСПИСАНИЕ =====
def scheduler():
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == '09:00':
            post_morning_prediction()
        elif now == '18:45':
            post_reaction()
        elif now == '22:30':
            post_summary()
        time.sleep(60)

# Уведомление при запуске
bot.send_message(ADMIN_ID, "✅ TotalControlBet Бот запущен и работает.")

# Запускаем планировщик в фоновом потоке
threading.Thread(target=scheduler, daemon=True).start()

# Запуск бота
bot.polling(none_stop=True)
