import math
def roots(a,b,c):
    dividendX1 = -b + math.sqrt((b * b) - (4.0 * a * c))
    dividendX2 = -b - math.sqrt((b * b) - (4.0 * a * c))
    divisor = 2.0 * a
    x1 = dividendX1/divisor
    x2 = dividendX2 / divisor
    print(x1)
    print(x2)

def printRoots():
    i = 10
    while i <= 10000:
        roots(1, i, 1)
        print(i)
        print('-----------------------')
        i = i * 10

#printRoots()

def roots2(a,b,c):
    dividend = -b - math.sqrt((b * b) - (4.0 * a * c))
    divisor = 2.0 * a
    x2 = dividend / divisor
    x1 = (c) / (a * x2)
    print(x1)
    print(x2)

def printRoots2():
    i = 10
    while True:
        roots2(1, i, 1)
        print(i)
        print('-----------------------')
        i = i * 10

printRoots2()