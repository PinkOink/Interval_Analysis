import numpy as np
from tolsolvty import tolsolvty
from scipy.optimize import linprog
import matplotlib.pyplot as plot


def solveISLAU():
    A = np.array([[3, 3, 9],
                  [5, 2, 6],
                  [4, 2, 6]])
    infA = A.copy()
    supA = A.copy()

    midb = np.array([0.5, -1, 5], ndmin = 2)
    radb = np.array([0.5, 1, 1], ndmin = 2)

    infb = midb - radb
    supb = midb + radb

    [tolmax, argmax, envs, ccode] = tolsolvty(infA, supA, np.transpose(infb), np.transpose(supb))
    print('tolmax = ', tolmax)
    print('argmax = ', argmax)
    print('envs = ', envs)
    print('ccode = ', ccode)
    print()

    c = np.array([0, 0, 0, 1, 1, 1])
    C = np.concatenate(
        (
            np.concatenate((-A, A), axis = 0),
            np.concatenate(
                (
                    -radb * np.identity(3),
                    -radb * np.identity(3)
                ), axis = 0)
        ), axis = 1)
    r = np.concatenate((-midb, midb), axis = 1)
    bounds = ((None, None),
              (None, None),
              (None, None),
              (0, None),
              (0, None),
              (0, None))

    print("No bounds solve:")
    print()
    simplex_res = linprog(c = c, A_ub = C, b_ub = r, method = 'simplex', bounds = bounds)
    print("Simplex solve:")
    print("Func value = ", simplex_res.fun)
    print("x = ", simplex_res.x[:3])
    print("w = ", simplex_res.x[3:])
    print()

    interior_point_res = linprog(c = c, A_ub = C, b_ub = r, method = 'interior-point', bounds = bounds)
    print("Interior point solve:")
    print("Func value = ", interior_point_res.fun)
    print("x = ", interior_point_res.x[:3])
    print("w = ", interior_point_res.x[3:])
    print()
    print()

    bounds = ((-0.44444444 + 0.0001, None),
              (None, None),
              (None, None),
              (0, None),
              (0, None),
              (0, None))
    print("x_0 bound solve:")
    print()
    simplex_res = linprog(c = c, A_ub = C, b_ub = r, method = 'simplex', bounds = bounds)
    print("Simplex solve:")
    print("Func value = ", simplex_res.fun)
    print("x = ", simplex_res.x[:3])
    print("w = ", simplex_res.x[3:])
    print()

    interior_point_res = linprog(c = c, A_ub = C, b_ub = r, method = 'interior-point', bounds = bounds)
    print("Interior point solve:")
    print("Func value = ", interior_point_res.fun)
    print("x = ", interior_point_res.x[:3])
    print("w = ", interior_point_res.x[3:])
    print()
    print()

    steps = np.arange(-2, 2, 0.2)
    x1_simplex_vals = []
    x1_interpoint_vals = []
    x3_simplex_vals = []
    x3_interpoint_vals = []
    w2_simplex_vals = []
    w2_interpoint_vals = []
    w_sum_simplex_vals = []
    w_sum_interpoint_vals = []
    for step in steps:
        bounds = ((None, None),
                  (step, step + 0.2),
                  (None, None),
                  (0, None),
                  (0, None),
                  (0, None))

        simplex_res = linprog(c=c, A_ub=C, b_ub=r, method='simplex', bounds=bounds)
        x1_simplex_vals.append(simplex_res.x[0])
        x3_simplex_vals.append(simplex_res.x[2])
        w2_simplex_vals.append(simplex_res.x[4])
        w_sum_simplex_vals.append(sum(simplex_res.x[3:]))

        interior_point_res = linprog(c=c, A_ub=C, b_ub=r, method='interior-point', bounds=bounds)
        x1_interpoint_vals.append(interior_point_res.x[0])
        x3_interpoint_vals.append(interior_point_res.x[2])
        w2_interpoint_vals.append(interior_point_res.x[4])
        w_sum_interpoint_vals.append(sum(interior_point_res.x[3:]))

    plot.figure()
    plot.plot(steps, x1_simplex_vals, label='x1')
    plot.plot(steps, x3_simplex_vals, label='x3')
    plot.plot(steps, w2_simplex_vals, label='w2')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_2 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Simplex (x_2) plot')
    plot.savefig('simplex(x_2).png', format='png')
    plot.show()

    plot.figure()
    plot.plot(steps, x1_interpoint_vals, label='x1')
    plot.plot(steps, x3_interpoint_vals, label='x3')
    plot.plot(steps, w2_interpoint_vals, label='w2')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_2 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Interior Point (x_2) plot')
    plot.savefig('interpoint(x_2).png', format='png')
    plot.show()


    x1_simplex_vals = []
    x1_interpoint_vals = []
    x2_simplex_vals = []
    x2_interpoint_vals = []
    w3_simplex_vals = []
    w3_interpoint_vals = []
    w_sum_simplex_vals = []
    w_sum_interpoint_vals = []
    for step in steps:
        bounds = ((None, None),
                  (None, None),
                  (step, step + 0.2),
                  (0, None),
                  (0, None),
                  (0, None))

        simplex_res = linprog(c=c, A_ub=C, b_ub=r, method='simplex', bounds=bounds)
        x1_simplex_vals.append(simplex_res.x[0])
        x2_simplex_vals.append(simplex_res.x[1])
        w3_simplex_vals.append(simplex_res.x[5])
        w_sum_simplex_vals.append(sum(simplex_res.x[3:]))

        interior_point_res = linprog(c=c, A_ub=C, b_ub=r, method='interior-point', bounds=bounds)
        x1_interpoint_vals.append(interior_point_res.x[0])
        x2_interpoint_vals.append(interior_point_res.x[1])
        w3_interpoint_vals.append(interior_point_res.x[5])
        w_sum_interpoint_vals.append(sum(interior_point_res.x[3:]))

    plot.figure()
    plot.plot(steps, x1_simplex_vals, label='x1')
    plot.plot(steps, x2_simplex_vals, label='x2')
    plot.plot(steps, w3_simplex_vals, label='w3')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_3 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Simplex (x_3) plot')
    plot.savefig('simplex(x_3).png', format='png')
    plot.show()

    plot.figure()
    plot.plot(steps, x1_interpoint_vals, label='x1')
    plot.plot(steps, x2_interpoint_vals, label='x2')
    plot.plot(steps, w3_interpoint_vals, label='w3')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_3 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Interior Point (x_3) plot')
    plot.savefig('interpoint(x_3).png', format='png')
    plot.show()


    x1_simplex_vals = []
    x1_interpoint_vals = []
    x2_simplex_vals = []
    x2_interpoint_vals = []
    x3_simplex_vals = []
    x3_interpoint_vals = []
    w2_simplex_vals = []
    w2_interpoint_vals = []
    w3_simplex_vals = []
    w3_interpoint_vals = []
    w_sum_simplex_vals = []
    w_sum_interpoint_vals = []
    steps = np.arange(-1, 1, 0.1)
    for step in steps:
        bounds = ((None, None),
                  (step, step + 0.2),
                  (step, step + 0.2),
                  (0, None),
                  (0, None),
                  (0, None))

        simplex_res = linprog(c=c, A_ub=C, b_ub=r, method='simplex', bounds=bounds)
        x1_simplex_vals.append(simplex_res.x[0])
        x2_simplex_vals.append(simplex_res.x[1])
        x3_simplex_vals.append(simplex_res.x[2])
        w2_simplex_vals.append(simplex_res.x[4])
        w3_simplex_vals.append(simplex_res.x[5])
        w_sum_simplex_vals.append(sum(simplex_res.x[3:]))

        interior_point_res = linprog(c=c, A_ub=C, b_ub=r, method='interior-point', bounds=bounds)
        x1_interpoint_vals.append(interior_point_res.x[0])
        x2_interpoint_vals.append(interior_point_res.x[1])
        x3_interpoint_vals.append(interior_point_res.x[2])
        w2_interpoint_vals.append(interior_point_res.x[4])
        w3_interpoint_vals.append(interior_point_res.x[5])
        w_sum_interpoint_vals.append(sum(interior_point_res.x[3:]))

    plot.figure()
    plot.plot(steps, x1_simplex_vals, label='x1')
    plot.plot(steps, x2_simplex_vals, label='x2')
    plot.plot(steps, x3_simplex_vals, label='x3')
    plot.plot(steps, w2_simplex_vals, label='w2')
    plot.plot(steps, w3_simplex_vals, label='w3')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_2 & x_3 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Simplex (x_2, x_3) plot')
    plot.savefig('simplex(x_2,x_3).png', format='png')
    plot.show()

    plot.figure()
    plot.plot(steps, x1_interpoint_vals, label='x1')
    plot.plot(steps, x2_interpoint_vals, label='x2')
    plot.plot(steps, x3_interpoint_vals, label='x3')
    plot.plot(steps, w2_interpoint_vals, label='w2')
    plot.plot(steps, w3_interpoint_vals, label='w3')
    plot.plot(steps, w_sum_simplex_vals, label='Sum(w)')
    plot.xlabel('x_2 & x_3 left border')
    plot.ylabel('Value')
    plot.legend()
    plot.title('Interior Point (x_2, x_3) plot')
    plot.savefig('interpoint(x_2,x_3).png', format='png')
    plot.show()



if __name__ == "__main__":
    solveISLAU()