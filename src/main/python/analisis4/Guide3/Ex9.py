def bisection(function, a, b, presition, n):
    pk = a
    for i in range(0, n):
        pk = (a+b)/2
        if (b-a)/2 < presition:
            break
        function_pk = function(pk)
        if function_pk == 0 or (b-a)/2 < presition:
            return pk
        elif function_pk * function(a) > 0:
            a = pk
        #elif function_pk * function(b) > 0:
        else:
            b = pk

    return pk




