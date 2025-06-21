from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import CallbackContext
from TotalControlBet_bot.config import ADMIN_CHAT_ID

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Бот запущен. Готов к работе!")

def status(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Бот активен и готов к публикации.")

def setup_handlers(dp):
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("статус", status))
