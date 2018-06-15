import os
import time
import pytz
import datetime


def get_time():
    tz=pytz.timezone('Asia/Shanghai')
    a=datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    return a
def bdwhile():
    with open("Shadow/1.txt") as her:
        he=her.readline()
    if int(he)==1:
        print("Welcome to the o&s system!")
        time.sleep(0.7)
        print("Just set some things,make a o&s system for you!")
        time.sleep(0.5)
        print("Your name: ",end='')
        aname=input()
        print("Your password: ",end='')
        apassword=input()
        print("Your age: ",end='')
        aage=input()
        print("Your email: ",end='')
        aemail=input()
        print("Your country: ",end='')
        acountry=input()
        print("Your city: ",end='')
        acity=input()
        print("Perpare you system",end='')
        time.sleep(0.5)
        print(".",end='')
        ppre="User:\n    Name:"+aname+"\n    Password:"+apassword+"\n    Age:"+aage+"\n    Email:"+aemail+"\n    Country:"+acountry+"\n    City:"+acity
        with open("Shadow/users.txt","w") as miao_shu:
            miao_shu.write(ppre)
        time.sleep(0.5)
        print(".",end='')
        with open("Shadow/1.txt","w") as gai:
            gai.write("2")
        time.sleep(0.5)
        print(".")
        lod=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        os.chdir(lod)
        lod=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        os.chdir(lod)
        os.chdir("users")
        os.mkdir(aname.title())
        os.chdir(aname.title())
        os.mkdir("Desktops")
        os.mkdir("Documents")
        os.mkdir("Downloads")
        os.mkdir(aname.lower())
        os.mkdir("Movies")
        os.mkdir("Pictures")
        os.mkdir("Publics")
        os.mkdir("Videos")
        time.sleep(0.5)
        print("Finished you own system!")
        print()
        lood=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        os.chdir(lood)
        os.chdir("users")
        os.chdir(aname.title())
    elif int(he)==2:
        tmei=get_time()
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as dt:
            msg="\n\nRun System at:"+tmei
            dt.write(msg)
        lood=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        os.chdir(lood)
        os.chdir("users")
        tmei=get_time()
