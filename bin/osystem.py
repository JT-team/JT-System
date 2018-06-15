import os
import time

import bdwhile

import Calculator

import help
import exit
import ftu
import cdu
import cdd
import fud
import mk


time.sleep(1)
print()
print("Power by o&s")
time.sleep(2)
print()
bdwhile.bdwhile()
while True:
    tmie=bdwhile.get_time()
    load=os.getcwd()
    print()
    print(load+"/ $",end=' ')
    ifmt=input()
    ifmtt=ifmt.rstrip().lstrip()
    ifmt=ifmt.lower().rstrip().lstrip()
    if ifmt=="help":
        help.help()
    elif ifmt=="exit":
        exit.exit()
        break
    elif ifmt=="ftu":
        ftu.ftu(load)
    elif ifmt=="cdu":
        load=cdu.cdu(load)
    elif ifmt=="cdd":
        load=cdd.cdd(load)
    elif ifmt=="fud":
        fud.fud()
        cday(load)
        with open("day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User want to found what things is or isn't exist."
            d.write(msg)
        a=1
    elif ifmt=='':
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User press 'Enter'."
            d.write(msg)
        pass
    elif ifmt=='mk':
        mk.mk()
        cday(load)
        with open("day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User want to make something."
            d.write(msg)
        a=1
    elif ifmt=='v.':
        cday(load)
        with open("day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User want to know what edition is this osystem is."
            d.write(msg)
        a=1
        print("o&s system")
        print("V.0.0.1F")
    elif ifmt=="gt":
        cday(load)
        with open("day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User want to know what time is it."
            d.write(msg)
        a=1
        print("Now is",tmie,".")
    elif ifmt=="./":
        print("What software do you want to open: ",end='')
        oen=input()
        if oen=="calculator":
            Calculator.calculator_runner()
        cday(load)
        with open("day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User want use a software. "+"(Extra:the software is:"+oen+")"
            d.write(msg)
        a=1
    else:
        print("foj:can't found information of '",ifmtt,"'")
        with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
            msg="\n["+tmie+"]:"+"User types "+ifmtt+"."
            d.write(msg)

        
#~Make and Think by Jason-Xu-Olycream~#
#~Help by David-Xu~#
#~V.0.1.2F~#
