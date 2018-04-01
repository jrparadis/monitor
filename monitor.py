from desktopmagic.screengrab_win32 import (saveScreenToBmp)
from PIL import Image
import pyautogui
import os
import time
import psutil

quality = 50
timeoutinseconds = 30
debug = True
last =  (0,0)
afk = 0
while(True):
    
    if pyautogui.position() == last:
        if afk == 0:
            #log to database
            afk = 1
        if debug is True:
            print ("afk?")

        time.sleep(timeoutinseconds)
    else:
        if afk == 1:
            #log to database
            afk = 0
        timey = str(time.time())
        newtime = timey.replace(".","")
        year = time.strftime("%Y")
        month = time.strftime("%B")
        day = time.strftime("%d")
        hour = "{}{}".format(time.strftime("%p"),time.strftime("%I"))
        minute = "{}{}".format(time.strftime("%M"),time.strftime("%S"))
        filename = "{}\{}\{}\{}\{}\{}.jpg".format(os.getcwd(),year,month,day,hour,minute)
        filename = filename.replace("\\","\\\\")
        dircheck = "{}\{}\{}\{}\{}".format(os.getcwd(),year,month,day,hour,minute)
        if not os.path.exists(dircheck):
            os.makedirs(dircheck)
        x = saveScreenToBmp(filename)
        newimage = Image.open(filename)
        newimage.thumbnail((1920, 540), Image.ANTIALIAS)
        newimage.save(filename, quality=quality)
        diskusage = os.path.getsize(filename)
        mult = 60 / timeoutinseconds
        kbaminute = round(diskusage/1000) * mult
        mbanhour = round((kbaminute * 60))/1000
        mbaday = round(mbanhour * 24)
        gbamonth = round(mbaday * 30)/1000
        if debug is True:
            ssamin = 60 / mult
            print("{} screenshots a minute | {} kb a minute | {} mb an hour | {} mb a day | {} gb a month".format(mult,kbaminute,mbanhour,mbaday,gbamonth))
            diskspace = round(psutil.disk_usage("F:").free/1000000000)
            print("{} gb free, that's enough for {} years".format(diskspace, round(int(diskspace/gbamonth)/12)))
        afk = 0
        last = pyautogui.position()
        time.sleep(timeoutinseconds)


