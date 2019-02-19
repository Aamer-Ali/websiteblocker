import time
from datetime import datetime as dt

host_path="/etc/hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

print(dt.now())  # Show date in format ---- 2019-02-19 10:36:49.543299 ----


while True:
    # In the if we are checking that is this the working hours basically we are comparing time here.
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hourse")
    else:
        print("Wow Working hours over .. You have access now ")
    time.sleep(5)
