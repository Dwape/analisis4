import math

def bisection(function, a, b, precision, max_iterations):
    for i in range(0, max_iterations):
        pk = (a+b)/2
        if function(pk) == 0 or (b - a) / 2 < precision:
            return pk
        if equal_sign(function(pk), function(a)):
            a = pk
        else:
            b = pk


def equal_sign(number1, number2):
    return number1*number2 > 0


def function1(x):
    return x**3-x-1


def function2(x):
    return (x**4)-2*(x**3)-4*(x**2)+4*x+4


def function3(x):
    return math.tan(x)-x


def function4(x):
    return x-2**(-x)


def function5(x):
    return x**3-25


def function6(x):
    return x**3-3

#print(bisection(function1, 1.0, 2.0, 10e-3, 1000))
#print(bisection(function2, -2, 0, 10e-8, 1000))
#print(bisection(function2, 0, 2, 10e-8, 1000))
#print(bisection(function2, 1, 2, 10e-8, 1000))
#print(bisection(function3, 4, 4.5, 10e-3, 1000))
#print(bisection(function4, 0, 1, 10e-3, 1000))
#print(bisection(function5, 2, 3, 10e-5, 1000))
#print(bisection(function6, 1, 2, 10e-5, 1000))
print(bisection(function1, 1.0, 2.0, 10e-5, 1000))