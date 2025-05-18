from apscheduler.schedulers.background import BackgroundScheduler
from app.views import coin_store_scheduler
from app.views import compare_order_and_coin_value_scheduler


def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    scheduler.add_job(coin_store_scheduler, 'interval', seconds=60)
    scheduler.add_job(compare_order_and_coin_value_scheduler, 'interval', seconds=3)
    scheduler.start()