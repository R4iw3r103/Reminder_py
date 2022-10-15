# from asyncio.timeouts import timeout
from plyer import notification
import time
import datetime

def remind():
  notification.notify(
    title = "白上フブキ",
    message = "「" + message_wanna_show + "」の時間ですよっ！",
    app_name = "Reminder",
    app_icon = r"C:\Users\stkin\Desktop\Study\Programming\Python\Reminder\Fubuki.ico",
    timeout = 10
    
  )

now_time = datetime.datetime.now()
message_wanna_show = input("リマインドしたいことを入力してください！: ")
print("次に、リマインドしてほしい時間を年、月、日、時、分ごとに入力してほしいですっ！")
year = input("年: ")
month= input("月: ")
date = input("日: ")
hour = input("時: ")
minute = input("分: ")
# time_wanna_execute = str(int(year), int(month), int(date), int(hour), int(minute))
# print(time_wanna_execute)
time_wanna_execute = datetime.datetime(int(year), int(month), int(date), int(hour), int(minute))
print(year + "年" + month + "月" + date + "日" + hour + "時" + minute + "分にリマインドしますね！")
sleep_time = (time_wanna_execute - now_time).total_seconds()
time.sleep(sleep_time)
remind()
