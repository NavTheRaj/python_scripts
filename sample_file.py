#!/usr/bin/env python3

with open('log.txt' ,'rt') as myfile:
    for myline in myfile:
        rid=myline.rfind('rid:')
        rip=myline.rfind('rip:')
        if rid>0:
            print('Mac->',myline[rid+5:])
        if rip>0:
            print('IP->',myline[rip+5:])
myfile.close()
