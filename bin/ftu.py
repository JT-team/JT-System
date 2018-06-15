import os
import time
import bdwhile

def ftu(load):
    tmie=bdwhile.get_time()
    zy=os.listdir(os.getcwd())
    for i in zy:
        pd=os.path.isdir(i)
        if pd==True:
            print("Folder     ",i)
        else:
            i=list(i)
            ppst=i[-4:]
            pst=""
            for i in ppst:
                pst=pst+i
            if ".txt"==pst:
                dp=os.path.getsize(i)
                if dp>=1024:
                    dp=dp/1024
                    if dp>=1024:
                        dp=dp/1024
                        if dp>=1024:
                            dp=dp/1024
                            if dp>=1024:
                                dp=dp/1024
                                if dp>=1024:
                                    dp=dp/1024
                                    print("TXT        ",i,"\t",dp,"P")
                                    continue
                                print("TXT        ",i,"\t",dp,"T")
                                continue
                            print("TXT        ",i,"\t",dp,"G")
                            continue
                        print("TXT        ",i,"\t",dp,"M")
                        continue
                    print("TXT        ",i,"\t",dp,"K")
                    continue
                print("TXT        ",i,"\t",dp,"B")
            if ".pdf"==pst:
                dp=os.path.getsize(i)
                if dp>=1024:
                    dp=dp/1024
                    if dp>=1024:
                        dp=dp/1024
                        if dp>=1024:
                            dp=dp/1024
                            if dp>=1024:
                                dp=dp/1024
                                if dp>=1024:
                                    dp=dp/1024
                                    print("PDF        ",i,"\t",dp,"P")
                                    continue
                                print("PDF        ",i,"\t",dp,"T")
                                continue
                            print("PDF        ",i,"\t",dp,"G")
                            continue
                        print("PDF        ",i,"\t",dp,"M")
                        continue
                    print("PDF        ",i,"\t",dp,"K")
                    continue
                print("PDF        ",i,"\t",dp,"B")
            if ".exe"==pst:
                dp=os.path.getsize(i)
                if dp>=1024:
                    dp=dp/1024
                    if dp>=1024:
                        dp=dp/1024
                        if dp>=1024:
                            dp=dp/1024
                            if dp>=1024:
                                dp=dp/1024
                                if dp>=1024:
                                    dp=dp/1024
                                    print("EXE        ",i,"\t",dp,"P")
                                    continue
                                print("EXE        ",i,"\t",dp,"T")
                                continue
                            print("EXE        ",i,"\t",dp,"G")
                            continue
                        print("EXE        ",i,"\t",dp,"M")
                        continue
                    print("EXE        ",i,"\t",dp,"K")
                    continue
                print("EXE        ",i,"\t",dp,"B")
            if ".jpg"==pst:
                dp=os.path.getsize(i)
                if dp>=1024:
                    dp=dp/1024
                    if dp>=1024:
                        dp=dp/1024
                        if dp>=1024:
                            dp=dp/1024
                            if dp>=1024:
                                dp=dp/1024
                                if dp>=1024:
                                    dp=dp/1024
                                    print("JPG        ",i,"\t",dp,"P")
                                    continue
                                print("JPG        ",i,"\t",dp,"T")
                                continue
                            print("JPG        ",i,"\t",dp,"G")
                            continue
                        print("JPG        ",i,"\t",dp,"M")
                        continue
                    print("JPG        ",i,"\t",dp,"K")
                    continue
                print("JPG        ",i,"\t",dp,"B")
    with open("/home/pi/System/0.0.2/bin/day.txt","a") as d:
        msg="\n["+tmie+"]:User wants to found what things is under the folder."
        d.write(msg)