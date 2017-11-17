def function(x, y):
    return (-0.25)*(x-y)


def runge_kutta(function, h, x0, y0, x):
    """Calculates the value of y(x0+h) using the Runge-Kutta method."""
    while x0 < x:
        f1 = h * function(x0, y0)
        f2 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f1)
        f3 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f2)
        f4 = h * function(x0 + h, y0 + f3)
        y0 += 1 / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
        x0 += h
    return y0


'''
def runge_kutta(function, h, x0, y0):
    """Calculates the value of y(x0+h) using the Runge-Kutta method."""
    f1 = h * function(x0, y0)
    f2 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f1)
    f3 = h * function(x0 + 1 / 2 * h, y0 + 1 / 2 * f2)
    f4 = h * function(x0 + h, y0 + f3)

    return y0 + 1 / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
'''




