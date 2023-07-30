import datetime
import time

def Bensons_Analog_clock():
    while True:
       ben = datetime.datetime.now()
       chenda = ben.strftime("%H:%M:%S")
       print("\r{}".format(chenda), end="")
       time.sleep(1)
Bensons_Analog_clock()