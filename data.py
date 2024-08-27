def openData(filename):
    X = []
    Y = []

    with open(filename, 'r') as file:
        for line in file:
            x, y = line.split(",")
            x = float(x)
            y = float(y)
            X.append(x)
            Y.append(y)

    return X, Y
