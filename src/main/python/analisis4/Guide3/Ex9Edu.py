import math


def bisection(function, a, b, precision, max_iterations):
    for i in range(0, max_iterations):
        pk = (a + b) / 2
        if function(pk) == 0 or (b - a) / 2 < precision:
            print(i)
            return pk
        if equal_sign(function(pk), function(a)):
            a = pk
        else:
            b = pk


def equal_sign(number1, number2):
    return number1 / math.fabs(number1) == number2 / math.fabs(number2)


def function(x):
    return x**3 - x - 1

#print(bisection(function, 1, 2, 10e-3, 1000000))


def funtionEx11(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

print(bisection(function, -2, 0, 10e-8, 10000000))
print(bisection(function, 0, 2, 10e-8, 10000000))
print(bisection(function, 1, 2, 10e-8, 10000000))