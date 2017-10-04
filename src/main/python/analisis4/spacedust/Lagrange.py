def lagrange(x_values, y_values):
    Lx = []
    for i in range(0, len(x_values)):
        Li = "(("
        for j in range(0, len(x_values)):
            if j != i:
                Li = Li + "(x-" + str(x_values[j]) + ")*"
        Li = Li[:-1]
        Li += ")"
        Li += "/("
        for j in range(0, len(x_values)):
            if j != i:
                Li = Li + "(" + str(x_values[i]) + "-" + str(x_values[j]) + ")*"
        Li = Li[:-1]
        Li += "))"
        Lx.append(Li)
    Px = ""
    for i in range(0, len(x_values)):
        Px += str(y_values[i]) + "*" + Lx[i] + "+"
    Px = Px[:-1]
    print(Px)
    return lambda x: eval(Px, {"x": x})


x_values = [1, 2, 4]
y_values = [1, 2, 4]

print(lagrange(x_values, y_values)(3))
