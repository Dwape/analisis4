from src.main.python.analisis4.Guide3.Ex1 import newton_raphson
import math

def function(x):
    return x**1/2


def derivate(x):
    return 1/(2*(x**(1/2)))

print(newton_raphson(2, function, derivate, 1e-4, 50))