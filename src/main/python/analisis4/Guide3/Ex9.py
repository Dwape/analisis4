def bisection(function, a, b, presition, n):
    pk = a
    for i in range(0, n):
        pk = (a+b)/2
        function_pk = function(pk)
        if function_pk == 0 or (b-a)/2 < presition:
            print(i)
            return pk
        elif function_pk * function(a) > 0:
            a = pk
        #elif function_pk * function(b) > 0:
        else:
            b = pk

    return pk


def function(x):
    return x**3 - x - 1

#print(bisection(function, 1, 2, 10e-3, 1000000))

def funtionEx11(x):
    return x**4 - 2*x**3 - 4*x**2 + 4*x + 4

print(bisection(function, -2, 0, 10e-3, 10000000))
print(bisection(function, 0, 2, 10e-3, 10000000))
print(bisection(function, 1, 2, 10e-3, 10000000))

