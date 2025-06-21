from telegram.ext import Updater
from TotalControlBet_bot.handlers import setup_handlers
from TotalControlBet_bot.config import TELEGRAM_TOKEN

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    setup_handlers(dp)
    updater.start_polling()
    print("Бот запущен ✅")
    updater.idle()

if __name__ == "__main__":
    main()
