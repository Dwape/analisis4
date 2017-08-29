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


def exercise5():
    x = 0.99
    for y in range(101):
        f = x**8 - 8*x**7 + 28*x**6 - 56*x**5 + 70*x**4 - 56*x**3 + 28*x**2 - 8*x +1
        g = (((((((x - 8)*x + 28)*x - 56)*x + 70)*x - 56)*x + 28)*x - 8)*x + 1
        h = (x-1)**8
        print('-----------------------------')
        print('{}{}{}'.format('f: ', f, '\n'))
        print('{}{}{}'.format('g: ', g, '\n'))
        print('{}{}{}'.format('h: ', h, '\n'))
        x += 1.98e-4

def exercise6a(array, x):
    sum = 0
    counter = 0
    for i in array:
        counter += 1
        sum += array[len(array)-counter] * x ** (counter-1)
    return sum

def exercise6b(array,x):
    sum =0
    counter =0
    for i in array:
        counter += 1
        sum += i*x**(len(array)-counter)
    return sum

def exercise6c(array,x):
    arrayB = []
    arrayB.append(array[0])

    for i in range(1, len(array)):
        arrayB.append(array[i] + arrayB[i-1]*x)

    return arrayB[len(arrayB)-1]


def exercise6():
    array = [2, 1, 2, 3, 4]
    x = [0, 10e-20, 10e-30, 10e-25, 10e-27, 10e20, 10e30, 10e25, 10e27]
    for i in x:
        print('{}{}{}'.format(i, ', A: ', exercise6a(array, i)))
        print('{}{}{}'.format(i, ', B: ', exercise6b(array, i)))
        print('{}{}{}'.format(i, ', C: ', exercise6c(array, i)))
        print('---------------------------------------------')


exercise6()