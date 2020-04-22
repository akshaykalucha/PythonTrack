from datetime import datetime
from Whatsapp import send_msg
from apscheduler.schedulers.blocking import BlockingScheduler
from Tracker import check_price
sched = BlockingScheduler()


price = check_price()


def start_sending():

    # Schedule job_function to be called every two hours
    sched.add_job(send_msg, args=price)

    sched.start()



if price>1:
    price = [str(price)]
    print('yes')
    start_sending()