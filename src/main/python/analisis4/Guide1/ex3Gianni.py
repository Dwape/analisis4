from decimal import Decimal

x = [2.718281828, -3.141592654, 1.414213562, 0.5772156649, 0.3010299957]
y = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]
w = [Decimal('2.718281828'), Decimal('-3.141592654'), Decimal('1.414213562'), Decimal('0.5772156649'), Decimal('0.3010299957')]
z = [Decimal('1486.2497'), Decimal('878366.9879'), Decimal('-22.37492'), Decimal('4773714.647'), Decimal('0.000185049')]
#x = [2.8, -3.1, 1, 0.57, 0.3]
#y = [1, 8, -2.2, 4, 0.1]
def exc3A():
    result = 0
    for i in range(len(x)):
        result += x[i]*y[i]
    print(result)

exc3A()

def exc3ADecimal():
    result = 0
    for i in range(len(w)):
        result += w[i]*z[i]
    print(result)

exc3ADecimal()

def exc3B():
    result = 0
    length = len(x)
    i=length-1
    while i >= 0:
        result += x[i]*y[i]
        i = i-1
    print(result)

#exc3B()

def exc3BDecimal():
    result = 0
    length = len(w)
    i=length-1
    while i >= 0:
        result += w[i]*z[i]
        i = i-1
    print(result)

exc3BDecimal()

def exc3C():
    fullList = x + y
    fullList.sort(reverse=True)
    sum1=0
    sum2=0
    for i in range(len(fullList)):
        if (fullList[i]<0.0):
            sum1 += fullList[i]
        else:
            sum2 += fullList[i]
    total = sum1+sum2
    print(total)
#exc3C()

def exc3CDecimal():
    fullList = w + z
    fullList.sort(reverse=True)
    sum1=0
    sum2=0
    for i in range(len(fullList)):
        if (fullList[i]<0.0):
            sum1 += fullList[i]
        else:
            sum2 += fullList[i]
    total = sum1+sum2
    print(total)
exc3CDecimal()

def exc3D():
    fullList = x + y
    fullList.sort()
    sum1=0
    sum2=0
    for i in range(len(fullList)):
        if (fullList[i]<0.0):
            sum1 += fullList[i]
        else:
            sum2 += fullList[i]
    total = sum1+sum2
    print(total)
#exc3D()

def exc3DDecimal():
    fullList = w + z
    fullList.sort()
    sum1=0
    sum2=0
    for i in range(len(fullList)):
        if (fullList[i]<0.0):
            sum1 += fullList[i]
        else:
            sum2 += fullList[i]
    total = sum1+sum2
    print(total)
exc3DDecimal()
