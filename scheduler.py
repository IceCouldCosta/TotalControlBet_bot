from apscheduler.schedulers.background import BackgroundScheduler
from TotalControlBet_bot.predictor import get_prediction
from TotalControlBet_bot.config import CHANNEL_USERNAME

def post_prediction(context):
    prediction = get_prediction()
    context.bot.send_message(chat_id=CHANNEL_USERNAME, text=prediction)

def setup_scheduler(updater):
    scheduler = BackgroundScheduler()
    scheduler.add_job(post_prediction, 'cron', hour=9, args=[updater.bot])
    scheduler.start()
