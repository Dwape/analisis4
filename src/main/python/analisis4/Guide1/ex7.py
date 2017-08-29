import math
from decimal import Decimal

def algorithm_1(n):
    """Calculates tn=1/(3^n)"""
    result = 1
    for i in range(1, n+1):
        result = result*3
    return 1/result

def algorithm_2(n):
    """Calculates tn=e^(n*ln3)"""
    return math.e**(-n*math.log(3))

def algorithm_3(n):
    """Calculates tn=(1/3)tn-1"""
    if n<1: return 1
    return (1/3)*algorithm_3(n-1)

def algorithm_4(n):
    """Calculates tn=(13/3)tn-1-(4/3)tn-2"""
    if n==0: return 1
    if n==1: return 1/3
    return (13/3)*algorithm_4(n-1)-(4/3)*algorithm_4(n-2)

def helper(list, algorithm):
    for i in range(len(list)):
        print(str(algorithm(list[i])))


#numbers = [1, 2, 3, 4, 5, 10, 25, 50, 100, 250, 500, 1000, 5000, 10000, 20000, 50000, 100000, 1000000]
#helper(numbers, algorithm_4)
#print(str(algorithm_2(3)))
#print(str(algorithm_3(3)))
#print(str(algorithm_4(3)))

def algorithm_1_decimal(n):
    """Calculates tn=1/(3^n)"""
    result = Decimal(1)
    for i in range(1, n+1):
        result = result*Decimal(3)
    return Decimal(1)/result

def algorithm_2_decimal(n):
    """Calculates tn=e^(n*ln3)"""
    return Decimal(math.e)**(Decimal(-n)*Decimal(math.log(3)))

def algorithm_3_decimal(n):
    """Calculates tn=(1/3)tn-1"""
    if n<1: return Decimal(1)
    return Decimal(1/3)*Decimal(algorithm_3(n-1))

def algorithm_4_decimal(n):
    """Calculates tn=(13/3)tn-1-(4/3)tn-2"""
    if n==0: return Decimal(1)
    if n==1: return Decimal(1/3)
    return Decimal(13/3)*Decimal(algorithm_4(n-1))-Decimal(4/3)*Decimal(algorithm_4(n-2))

def helper(list, algorithm):
    for i in range(len(list)):
        print(str(algorithm(list[i])))

numbers = [1, 2, 3, 4, 5, 10, 25, 50, 100, 250, 500, 1000, 5000, 10000, 20000, 50000, 100000, 1000000]
helper(numbers, algorithm_4_decimal)