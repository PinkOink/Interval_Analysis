from numpy import loadtxt, transpose, arange, array, zeros, size, maximum, ones, argmin
from tolsolvty import tolsolvty
from matplotlib.pyplot import figure, savefig, show


def calcf(x, infA, supA, infb, supb):
    Ac = 0.5 * (infA + supA)
    Ar = 0.5 * (supA - infA)
    bc = 0.5 * (infb + supb)
    br = 0.5 * (supb - infb)

    ms = size(supA, 0)

    weight = ones((ms, 1))

    absx = abs(x)

    Acx = Ac @ x
    Arabsx = Ar @ absx

    infs = bc - (Acx - Arabsx)
    sups = bc - (Acx + Arabsx)

    tt = weight * (br - maximum(abs(infs), abs(sups)))

    mc = argmin(tt)
    f = tt[mc]

    return f


def plot_tol(infA, supA, infb, supb, argmax, tolmax):
    x = arange(-0.2, 1.4, 0.01)
    y = arange(-1.2, 0.4, 0.01)
    sh = x.shape[0]
    z = zeros((sh, sh))

    for i in range(sh):
        for j in range(sh):
            arr = array([[x[i]], [y[j]]])
            z[i, j] = calcf(arr, infA, supA, infb, supb)

    fig = figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(argmax[0], argmax[1], tolmax, 'ro', label='Arg Max')
    ax.contour(x, y, z)
    ax.set_xlabel('x_1')
    ax.set_ylabel('x_2')
    ax.set_zlabel('Tol(x_1, x_2)')
    ax.set_zlim(-8, 1.5)
    savefig('Tol(x_1, x_2)' + '.png', format='png')
    show()


def solveISLAU():
    path_folder = 'task'

    infA = loadtxt(path_folder + '/infA.txt')
    supA = loadtxt(path_folder + '/supA.txt')

    infb1 = loadtxt(path_folder + '/infb1.txt', ndmin=2)
    supb1 = loadtxt(path_folder + '/supb1.txt', ndmin=2)

    [tolmax, argmax, envs, ccode] = tolsolvty(infA, supA, infb1, supb1)
    print("Part 1")
    print('tolmax = ', tolmax)
    print('argmax = ', argmax)
    print('envs = ', envs)
    print('ccode = ', ccode)
    print()


    infb2 = loadtxt(path_folder + '/infb2.txt', ndmin=2)
    supb2 = loadtxt(path_folder + '/supb2.txt', ndmin=2)

    [tolmax, argmax, envs, ccode] = tolsolvty(transpose(infA), transpose(supA), infb2, supb2)
    print("Part 2")
    print('tolmax = ', tolmax)
    print('argmax = ', argmax)
    print('envs = ', envs)
    print('ccode = ', ccode)
    print()

    plot_tol(transpose(infA), transpose(supA), infb2, supb2, argmax, tolmax)


if __name__ == "__main__":
    solveISLAU()