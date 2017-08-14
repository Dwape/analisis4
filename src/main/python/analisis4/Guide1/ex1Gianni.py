
from math import e, inf
import sys
def excCiii():
    i=1
    while(True):
        number = e**(-i)
        print(number)
        if(number==0.0): sys.exit()
        print(i)
        i+=1

#excCiii()

def excA():
    i=1.0
    while i != inf:
        print(i)
        i=i*10

#excA()

def excB():
    i = 1.0
    while (i != 0.0):
        print(i)
        i = i / 10

excB()