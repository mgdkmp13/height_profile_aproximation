from data import *
from interpolation import *
import matplotlib.pyplot as plt


def zad1_lagrange(X, Y, nPoints):
    # lagrange linear node
    nodesIndices = list(map(int, linear_nodes(0, len(X) - 1, nPoints)))
    xLagrange = []
    yLagrange = []
    for i in nodesIndices:
        xLagrange.append(X[i])
        yLagrange.append(Y[i])

    yLinearInter = []
    for i in range(len(X)):
        yLinearInter.append(lagrange(X[i], xLagrange, yLagrange))

    plt.plot(X, Y, label="Original function")
    plt.plot(X, yLinearInter, color="orange", label="Lagrange interpolation")
    plt.scatter(xLagrange, yLagrange, color="red", label="Linear nodes")
    plt.title("Lagrange interpolation with linear nodes")
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m ASL]")
    plt.legend()
    plt.savefig("lagrange_spline_" + str(nPoints) + ".png")
    plt.show()

    # lagrange chebyshev nodes
    xChebyshev, yChebyshev = chebyshev_nodes(X, Y, nPoints)
    y_interpolated = []
    for i in range(len(X)):
        y_interpolated.append(lagrange(X[i], xChebyshev, yChebyshev))

    plt.plot(X, Y, label="Original function")
    plt.plot(X, y_interpolated, color="green", label='Lagrange interpolation')
    plt.scatter(xChebyshev, yChebyshev, color='red', label='Chebyshev nodes')
    plt.title("Lagrange interpolation with chebyshev nodes")
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m ASL]")
    plt.legend()
    plt.savefig("lagrange_spline_cheb_" + str(nPoints) + ".png")
    plt.show()


def zad2_spline(X, Y, nPoints):
    nodesIndices = list(map(int, linear_nodes(0, len(X), nPoints)))
    xNodes = []
    yNodes = []
    for i in nodesIndices:
        if i > len(X) - 1:
            i = len(X) - 1
        xNodes.append(X[i])
        yNodes.append(Y[i])
    coefficients = cubic_spline(xNodes, yNodes)

    yInterpolated = []

    for xInter in X:
        for i in range(len(xNodes)-1):
            if xNodes[i] <= xInter <= xNodes[i + 1]:
                a, b, c, d = coefficients[i * 4: i * 4 + 4]
                yInterpolated.append(a + b * (xInter - xNodes[i]) + c * (xInter - xNodes[i]) ** 2 + d * (xInter - xNodes[i]) ** 3)
                break

    plt.plot(X, Y, label='Original function')
    plt.plot(X, yInterpolated, color="green", label='Cubic Spline Linear Interpolation')
    plt.scatter(xNodes, yNodes, color='red', label='Spline Nodes')
    plt.legend()
    plt.xlabel("Distance [m]")
    plt.ylabel("Height [m ASL]")
    plt.title("Cubic spline interpolation with linear nodes")
    plt.savefig("cubic_spline_" + str(nPoints) + ".png")
    plt.show()


def main():
    X, Y = openData("./2018_paths/genoa_rapallo.txt")
    X1, Y1 = openData("./2018_paths/WielkiKanionKolorado.csv")
    X2, Y2 = openData("./2018_paths/rozne_wniesienia.txt")
    X3, Y3 = openData("./2018_paths/MountEverest.csv")
    X4, Y4 = openData("./2018_paths/SpacerniakGdansk.csv")
    N = [5, 10, 25, 100]
    for n in N:
        zad1_lagrange(X2, Y2, n)
        zad2_spline(X4, Y4, n)


if __name__ == '__main__':
    main()
