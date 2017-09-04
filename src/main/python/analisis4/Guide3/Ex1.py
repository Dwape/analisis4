import math

def newton_raphson(x0, function, function_derivate, bound, max):
    x1 = x0 - function(x0) / function_derivate(x0)
    for i in range(0, max):
        if math.fabs(x1 - x0) < bound:
            return x1
        x0 = x1
        x1 = x0 - function(x0) / function_derivate(x0)
    return x1


def function(x):
    return x-math.exp(-x)


def function_derivate(x):
    return 1+math.exp(-x)
