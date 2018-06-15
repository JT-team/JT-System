import os
from settings import Settings

a=Settings()
def help():
    print("|------------------------------------------------------------------------------------------------------help------------------------------------------------------------------------------------------------------|")
    print("                                                                                     If you want help, press 'help' for help.")
    print("                                                                                     If you want quit, press 'exit' for quit.")
    print("                                                                                    If you want go up one folder, press 'cdu'.")
    print("                                                                                   If you want to make some thing, press 'mk'.")
    print("                                                                                   If you want go down one folder, press 'cdd'.")
    print("                                                                             If you want to know things under the folder, press 'ftu'.")
    print("                                                                             If you want found something is or is't exist,press 'fud'.")
    print("                                                                          If you want found things under the folder, press 'fud' for seach.")
    print("                                                                 foj is a kind of 'Trace back' that can tell you what wrong was the information have.")
    print("                                                             Make and think by jun hao Xu.If you have any question,tell me by the email:xujunhao61@163.com")
    load=os.getcwd()
    with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
        msg="\n["+a.time+"]:User wants to have some help."
        d.write(msg)