from decimal import Decimal

def gaussLegendre(deviation):
    a = 1
    b = 1/(2**(1/2))
    t = 1/4
    p = 1

    while (a-b) > deviation:
        x = (a+b)/2
        y = (a*b)**(1/2)
        t = t-(p*(a-x)**2)
        a = x
        b = y
        p = 2*p

    return ((a+b)**2)/(4*t)


def gaussLegendreDecimal(deviation):
    a = Decimal('1')
    b = Decimal('1')/(Decimal('2')**(Decimal('1')/Decimal('2')))
    t = Decimal('1')/Decimal('4')
    p = Decimal('1')

    while (a-b) > deviation:
        x = (a+b)/Decimal('2')
        y = (a*b)**(Decimal('1')/Decimal('2'))
        t = t-(p*(a-x)**Decimal('2'))
        a = x
        b = y
        p = 2*p

    return ((a+b)**Decimal('2'))/(Decimal('4')*t)


print(gaussLegendre(0.00000000000001))
print(gaussLegendreDecimal(0.00000000001))