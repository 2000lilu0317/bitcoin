from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from cms.module.get_data import get_all_data
from cms.module.train import train

def update():
   """
   This function is called by start() below
   """
   train("btn")
   train("eth")
   get_all_data() # 若干重いが、とりあえず今はここでデータを取ってくる
   print('Update!')

def start():
   """
   Scheduling data update
   Run update function once every 12 seconds
   """
   scheduler = BackgroundScheduler()
   
   scheduler.add_job(update, 'interval', seconds=1800) # schedule
   scheduler.start()