from src.main.python.analisis4.Guide3.Ex1 import newton_raphson
import math

def functionA(x):
    return x**3 - 2*x**2 - 5


def derivateA(x):
    return 3*x**2 - 4*x


print(newton_raphson(4, functionA, derivateA, 0.0001, 100))


def functionB(x):
    return x-math.cos(x)


def derivateB(x):
    return 1+math.sin(x)

print(newton_raphson(math.pi/2, functionB, derivateB, 1e-4, 50))


def functionC(x):
    return x**3 + 3*x**2 - 1


def derivateC(x):
    return 3*x**2 + 6*x


print(newton_raphson(-4, functionC, derivateC, 1e-4, 50))