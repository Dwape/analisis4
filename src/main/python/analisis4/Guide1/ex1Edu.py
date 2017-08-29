import math

def lim_e_x():
    """lim(x->inf) e^x , breaks when number is too large."""
    i = 0
    while True:
        print(i)
        print(math.e**i)
        i += 1


#lim_e_x() #8.218407461554662e+307 for x=709

def value_of_e(n):
    for i in range(1, n+1):
        aprox = (1+(1/i))**i
        print('{}{}{}{}{}'.format(i, ': ', aprox, '  error  ', math.e-aprox))

def value_of_e_2(n):
    aprox = (1+(1/n))**n
    print('{}{}{}{}{}'.format(n, ': ', aprox, '  error  ', math.e - aprox))

def value_of_e_i():
    n = 10
    while n<10e25+1:
        aprox = (1+(1/n))**n
        print('{}{}{}{}{}'.format(n, ': ', aprox, '  error  ', math.e - aprox))
        n *= 10

def value_of_e_ii():
    n = 160e5
    while n < 170e5+1:
        aprox = (1+(1/n))**n
        print('{}{}{}{}{}'.format(n, ': ', aprox, '  error  ', math.e - aprox))
        n += 1e5

def value_of_e_iii():
    n = 16777200
    while n < 16777251:
        aprox = (1 + (1 / n)) ** n
        print('{}{}{}{}{}'.format(n, ': ', aprox, '  error  ', math.e - aprox))
        n += 1

#value_of_e(100000)
#value_of_e_2(100000)
#value_of_e_i()
#value_of_e_ii()
#value_of_e_iii()







