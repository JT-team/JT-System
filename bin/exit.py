import time,bdwhile,os

def exit():
    tmie=bdwhile.get_time()
    with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
        msg="\n["+tmie+"]:"+"User wants to exit."
        d.write(msg)
    print("breaking",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
    print(".",end='')
    time.sleep(0.5)
    
load=os.getcwd()
print(load)