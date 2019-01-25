import os
import time


def ls():
    zy = os.listdir(os.getcwd())
    for i in zy:
        pd = os.path.isdir(i)
        if pd is True:
            time.sleep(0.1)
            print("Folder     ", i)
        else:
            time.sleep(0.1)
            if ".txt" in i:
                dp = os.path.getsize(i)
                if dp >= 1024:
                    dp = dp / 1024
                    if dp >= 1024:
                        dp = dp / 1024
                        if dp >= 1024:
                            dp = dp / 1024
                            if dp >= 1024:
                                dp = dp / 1024
                                if dp >= 1024:
                                    dp = dp / 1024
                                    print("File       ", i, "\t", dp, "P")
                                    continue
                                print("TXT       ", i, "\t", dp, "T")
                                continue
                            print("TXT       ", i, "\t", dp, "G")
                            continue
                        print("TXT       ", i, "\t", dp, "M")
                        continue
                    print("TXT       ", i, "\t", dp, "K")
                    continue
                print("TXT       ", i, "\t", dp, "B")
