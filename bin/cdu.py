import os
import bdwhile

def cdu(load):
    tmie=bdwhile.get_time()
    if load=="/home/pi/System/0.0.2/":
        print("foj:cdu can't work information cucessful because this is the last catalog.")
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User wants go up one folder but it's the last catalog."
            d.write(msg)
    else:
        load=os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
        os.chdir(load)
        print("cd work cucessful,and finished you information.")
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User wants go up one folder."
            d.write(msg)
        return load
