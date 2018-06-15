import os

def fud():
    print("Which file/foulder do you want found: ",end='')
    ound=input()
    pd=os.path.exists(ound)
    if pd==True:
        print("'",ound,"'","is exist.")
    else:
        print("'",ound,"'","isn't exist")