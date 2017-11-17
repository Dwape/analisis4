def function(x,y):
    return (-0,25)*(x-y)

def runge_Kutta(x,y,h):
    f1 = h*function(x,y)
    f2 = h*function(x + 1/2 * h, y + 1/2 * f1)
    f3 = h*function(x + 1/2 * h, y + 1/2 * f2)
    f4 = h*function(x + h, y + f3)

    return y + 1/6 * (f1+ 2*f2 + 2*f3 + f4)
