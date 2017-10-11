#!/usr/bin/env python
import datetime
import os
import platform

today = datetime.datetime.today()
today_num = today.weekday()

platform = platform.platform()
if "Darwin" in platform:

    while today_num == 2:
        os.system("say it is wednesday my dudes!")
    else:
	    os.system("say My dudes, it is not Wednesday.")
else:
    print("Buy a Mac, my dudes.")
