import numpy as np

def linear_nodes(x1, x2, n):
    diff = (x2 - x1) / (n-1)
    nodes = [x1]
    last = x1
    for i in range(n-1):
        nodes.append(last + diff)
        last += diff

    return nodes

def chebyshev_nodes(X, Y, N):
    if N <= 1:
        return [X[0]], [Y[0]]
    else:
        xNodes = np.zeros(N)
        yNodes = np.zeros(N)
        for i in range(N):
            chebyshev = np.cos(((2*i + 1) * np.pi) / (2*N))
            index = int(round(0.5 * (chebyshev + 1) * (len(X) - 1)))
            xNodes[i] = (X[index])
            yNodes[i] = (Y[index])
        return xNodes, yNodes


def lagrange(x, xNodes, yNodes):
    result = 0
    for i in range(len(xNodes)):
        base = 1
        for j in range(len(xNodes)):
            if i is not j  and xNodes[i] != xNodes[j]:
                base *= (x - xNodes[j]) / (xNodes[i] - xNodes[j])
        result += (yNodes[i] * base)
    return result


def cubic_spline(xNodes, yNodes):
    n = len(xNodes) - 1  # liczba podprzedzialow
    A = []
    b = []

    # pierwsza kropeczka
    row = np.zeros(4 * n)
    row[0] = 1  # a0
    A.append(row)
    b.append(yNodes[0])

    # druga kropeczka
    row = np.zeros(4 * n)
    h = xNodes[1] - xNodes[0]
    row[0] = 1
    row[1] = h
    row[2] = h ** 2
    row[3] = h ** 3
    A.append(row)
    b.append(yNodes[1])

    # pętlowe rzeczy
    # pętlowe rzeczy
    for i in range(1, n):
        # pierwsza kropeczka
        row = np.zeros(4 * n)
        row[4 * i] = 1
        A.append(row)
        b.append(yNodes[i])

        # druga kropeczka
        row = np.zeros(4 * n)
        h = xNodes[i + 1] - xNodes[i]
        row[4 * i] = 1
        row[4 * i + 1] = h
        row[4 * i + 2] = h ** 2
        row[4 * i + 3] = h ** 3
        A.append(row)
        b.append(yNodes[i + 1])

        # trzecia kropeczka
        row = np.zeros(4 * n)
        h = xNodes[i] - xNodes[i - 1]
        row[4 * (i - 1) + 1] = 1  # b0
        row[4 * (i - 1) + 2] = 2 * h  # c0
        row[4 * (i - 1) + 3] = 3 * (h ** 2)  # d0
        row[4 * (i - 1) + 5] = -1  # b1
        A.append(row)
        b.append(0)

        # czwarta kropeczka
        row = np.zeros(4 * n)
        h = xNodes[i] - xNodes[i - 1]
        row[4 * (i - 1) + 2] = 2  # c0
        row[4 * (i - 1) + 3] = 6 * h  # d0
        row[4 * (i - 1) + 6] = -2  # c1
        A.append(row)
        b.append(0)

    # piata kropeczka
    row = np.zeros(4 * n)
    row[2] = 1  # c0
    A.append(row)
    b.append(0)
    row = np.zeros(4 * n)
    row[4 * n - 1] = 6 * (xNodes[-1] - xNodes[-2])  # dn
    row[4 * n - 2] = 2  # cn
    A.append(row)
    b.append(0)

    coefficients = np.linalg.solve(A, b)
    return coefficients