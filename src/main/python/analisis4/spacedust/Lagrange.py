def lagrange(x_values, y_values):
    """Lagrange method. Returns a function that interpolates the points provided as function
    parameters. This function can be evaluated in a value of x to get its estimated y value."""
    lx = []
    for i in range(0, len(x_values)):
        li = ""
        ld = ""
        for j in range(0, len(x_values)):
            if j != i:
                li += "(x-" + str(x_values[j]) + ")*"
                ld += "(" + str(x_values[i]) + "-" + str(x_values[j]) + ")*"
        li = li[:-1]
        Lc = ld[:-1]
        lx.append("(" + li + ")/(" + Lc + ")")
    Px = ""
    for i in range(0, len(x_values)):
        Px += str(y_values[i]) + "*" + lx[i] + "+"
    Px = Px[:-1]
    return lambda x: eval(Px, {"x": x})