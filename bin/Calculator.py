import time
import math

def calculator_runner():
    def jia(a,b):
        c=a+b
        return c
    def jian(a,b):
        c=a-b
        return c
    def chen(a,b):
        c=a*b
        return c
    def chu(a,b):
        c=a/b
        return c
    def chen_fang(a,b):
        c=math.pow(a,b)
        return c
    def kai_fang(a):
        b=int(math.sqrt(a))
        return b
        
        
    print("----------Welcome to o&s calculator----------")
    time.sleep(1)
    while True:
        print("                   +:1\n                   -:2\n                   *:3\n                   /:4\n                  x**y:5\n                 x=?**?:6")
        time.sleep(1)
        print("choose:1/2/3/4/5/6('q' for quit): ",end='')
        chose=input()
        if chose=="1":
            print("First number: ",end='')
            fn=int(input())
            print("Second number: ",end='')
            sn=int(input())
            he=jia(fn,sn)
            print(fn,"+",sn,"=",he)
        elif chose=="2":
            print("First number: ",end='')
            fn=int(input())
            print("Second number: ",end='')
            sn=int(input())
            he=jian(fn,sn)
            print(fn,"-",sn,"=",he)
        elif chose=="3":
            print("First number: ",end='')
            fn=int(input())
            print("Second number: ",end='')
            sn=int(input())
            he=chen(fn,sn)
            print(fn,"*",sn,"=",he)
        elif chose=="4":
            print("First number: ",end='')
            fn=int(input())
            print("Second number: ",end='')
            sn=int(input())
            he=chu(fn,sn)
            print(fn,"/",sn,"=",he)
        elif chose=="5":
            print("First number: ",end='')
            fn=int(input())
            print("Second number: ",end='')
            sn=int(input())
            he=chen_fang(fn,sn)
            print(fn,"**",sn,"=",he)
        elif chose=="6":
            print("Number: ",end='')
            fn=int(input())
            he=kai_fang(fn)
            print("√￣",fn,"≈=",he)
        elif chose=="q":
            print("Thank for used")
            time.sleep(1)
            break
        else:
            print("Wrong information")
