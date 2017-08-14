import math

def exercise1C(n):
    x = 1
    for y in range(n):
        x /= 10
    print(1 / x)
    print(x)

def exercise2(n,x):
    h = 1.0
    for y in range(n):
        h /= 10
        cos = (math.cos(x + h) - math.cos(x)) / h
        sen = (math.sin(x+h)-math.sin(x))/h
        x2 = ((x + h)**2.0 - x**2.0) / h
        print('{}{}{}{}{}{}{}{}'.format('n: ', y, "--cos: ", cos, "--sen: ", sen, "--X: ", x2))

