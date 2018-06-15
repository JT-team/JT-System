import os,bdwhile
from cdu import cdu

def cdd(load):
    tmie=bdwhile.get_time()
    print("Which folder do you want down:",end=' ')
    foder=input()
    try:
        os.chdir(foder)
    except:
        print("foj:Couldn't found folder name '",foder,"'.")
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User wants go down to "+foder+" folder but "+foder+" isn't exists."
            d.write(msg)
    else:
        load=os.getcwd()
        print("cdd work cucessful.")
        load=load+"/"+foder
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User wants go down to "+foder+" folder."
            d.write(msg)
        return load