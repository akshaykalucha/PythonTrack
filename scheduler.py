from datetime import datetime
from Whatsapp import send_msg
from apscheduler.schedulers.blocking import BlockingScheduler



sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=10)

sched.start()