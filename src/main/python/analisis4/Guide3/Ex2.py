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

def functionD(x):
    return x-0.8-0.2*math.sin(x)


def derivateD(x):
    return 1-0.2*math.cos(x)

print(newton_raphson(math.pi/2, functionD, derivateD, 1e-4, 50))

def functionE(x):
    return x**3-x-1


def derivateE(x):
    return 3*x**2-1

print(newton_raphson(2, functionE, derivateE, 1e-4, 50))

def function3(x):
    return


def derivate3(x):
    return 1/(2*math.sqrt(x))

print(newton_raphson(2, function3, derivate3, 1e-4, 50))




def functionE(x):
    return x**3-x-1


def derivateE(x):
    return 6*x


print(newton_raphson(2, functionE, derivateE, 1e-4, 50))


