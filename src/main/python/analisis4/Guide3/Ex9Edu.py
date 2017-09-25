import math


def bisection(function, a, b, precision, max_iterations):
    for i in range(0, max_iterations):
        pk = (a + b) / 2
        if function(pk) == 0 or (b - a) / 2 < precision:
            return pk
        if equal_sign(function(pk), function(a)):
            a = pk
        else:
            b = pk


def equal_sign(number1, number2):
    return number1 / math.fabs(number1) == number2 / math.fabs(number2)
