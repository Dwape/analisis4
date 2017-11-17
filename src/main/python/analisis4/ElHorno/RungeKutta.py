def runge_kutta(function, h, x0, y0, x, tm):
    """Calculates the value of y(x0+h) using the Runge-Kutta method
    for Newton's law of cooling, where tm is the temperature of the environment."""
    while x0 < x:
        f1 = h * function(y0, tm)
        f2 = h * function(y0 + 1 / 2 * f1, tm)
        f3 = h * function(y0 + 1 / 2 * f2, tm)
        f4 = h * function(y0 + f3, tm)
        y0 += 1 / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
        x0 += h
    return y0


def temperature_function(y, tm):
    return -0.25 * (y - tm)


#print(runge_kutta(temperature_function, 0.1, 0, 150, 5, 62.25))

'''
def runge_kutta(function, h, x0, y0):
    """Calculates the value of y(x0+h) using the Runge-Kutta method."""
    f1 = h * function(x0, y0)
    f2 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f1)
    f3 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f2)
    f4 = h * function(x0 + h, y0 + f3)

    return y0 + 1 / 6 * (f1 + 2 * f2 + 2 * f3 + f4)

def runge_kutta2(function, h, x0, y0, x):
    """Calculates the value of y(x0+h) using the Runge-Kutta method."""
    while x0 < x:
        f1 = h * function(x0, y0)
        f2 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f1)
        f3 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f2)
        f4 = h * function(x0 + h, y0 + f3)
        y0 += 1 / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
        x0 += h
    return y0

def function1(x, y, tm):
    return -0.25 * (y - tm)
'''




