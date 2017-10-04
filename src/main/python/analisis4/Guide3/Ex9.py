import math

def bisection(function, a, b, presition, n):
    pk = a
    for i in range(0, n):
        pk = (a+b)/2
        function_pk = function(pk)
        if function_pk == 0 or (b-a)/2 < presition:
            print(i+1)
            return pk
        elif function_pk * function(a) > 0:
            a = pk
        #elif function_pk * function(b) > 0:
        else:
            b = pk

    return pk


def function(x):
    return x**3 - x - 1

print(bisection(function, 1, 2, 10e-5, 1000000))

def funtionEx11(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

#print(bisection(function, -2, 0, 10e-3, 10000000))
#print(bisection(function, 0, 2, 10e-3, 10000000))
#print(bisection(function, 1, 2, 10e-3, 10000000))

def functionEx12(x):
    return x-math.tan(x)

#print(bisection(functionEx12, 4, 4.5, 10e-3, 10000000))

def functionEx12b(x):
    return x-2**(-x)

#print(bisection(functionEx12b, 0, 1, 10e-3, 10000000))

def functionEx12c(x):
    return  math.e**x - x**2 + 3*x - 2

#print(bisection(functionEx12c, 0, 1, 10e-3, 10000000))

def functionEx12d(x):
    return  math.e**x + 2**-x + 2*math.cos(x) - 6

#print(bisection(functionEx12d, 1, 2, 10e-3, 10000000))

def functionEx13(x):
    return  x**3-25

#print(bisection(functionEx13, 2, 3, 10e-5, 10000000))

def functionEx14(x):
    return  x**3-3

print(bisection(functionEx14, 1, 2, 10e-5, 10000000))


