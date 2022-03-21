from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from cms.module.get_data import get_all_data
from cms.module.train import train

def update():
   get_all_data() 
   train("btn")
   train("eth")
   print('Update!')

def start():
   """
   Scheduling data update
   Run update function once every 12 seconds
   """
   scheduler = BackgroundScheduler()
   
   scheduler.add_job(update, 'interval', seconds=3600) # schedule
   scheduler.start()