import os
import time

import ls
import power_off

time.sleep(1)
print("Power by o&s")
time.sleep(2)
print()
while True:
    load = os.getcwd()
    print(load + " $", end=' ')
    ifmt = input()
    ifmtt = ifmt.rstrip().lstrip()
    ifmt = ifmt.lower().rstrip().lstrip()
    if ifmtt == "ls":
        ls.ls()
    elif ifmtt == "poweroff":
        power_off.poweroff()
        break
    elif ifmtt == "":
        pass
    else:
        print("Unknown object. Enter \"help\" for some advice.")

# ~Make and Think by Jason-Xu-Olycream~#
# ~Help by David-Xu~#
# ~V.0.1.2F~#
