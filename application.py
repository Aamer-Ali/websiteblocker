# I have added a copy of host file for testing purpose....

import time
import os
from datetime import datetime as dt

host_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]


# print(dt.now())  # Show date in format ---- 2019-02-19 10:36:49.543299 ----

while True:
    # In the if we are checking that is this the working hours basically we are comparing time here.
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          16):
        print("Working hours")
        with open(host_path, 'r+') as file:
            content = file.read()
            for websites in website_list:
                if websites in content:
                    pass
                else:
                    file.write("")
                    file.write(redirect + " " + websites + "\n")
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(websites in line for websites in website_list):
                    file.write(line)
            file.truncate()
        print("Wow Working hours over .. You have access now ")
    time.sleep(5)
