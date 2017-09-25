def bisection(function, a, b, presition, n):
    pk = a
    for i in range(0, n):
        pk = (a+b)/2
        if pk < presition:
            break
        if function(pk) * function(a) > 0:
            b = pk
        elif function(pk) * function(b) < 0:
            a = pk
        else:
            return pk
    return pk


