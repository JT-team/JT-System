import os

def mk():
    load=os.getcwd()
    print("Do you want make a folder or a file: ",end='')
    chose=input()
    chose=chose.rstrip().lstrip().lower()
    if chose=="file":
        print("What name of the file do you want to make: ",end='')
        nm=input()
        with open(load+'/'+nm,"w"):
            pass
        print("mk work cucessful.")
    elif chose=="folder":
        print("What name of the folder do you want to make: ",end='')
        nm=input()
        if nm=='':
            print("foj:can't use Null for folder name.")
        else:
            os.mkdir(nm)
            print("mk work cucessful.")
    else:
        print("foj:unknow type.")