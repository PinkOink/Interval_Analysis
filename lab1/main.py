from kaucherpy import Kaucher as interval
import numpy as np
import numpy.linalg as la


def count_interval_det_2x2_matrix(eps):
    a11 = a12 = a22 = interval(1 - eps, 1 + eps)
    a21 = interval(1.1 - eps, 1.1 + eps)

    return a11 * a22 - a12 * a21


def beck_criteria(A):
    _n = len(A)
    A_med = np.zeros((_n, _n))
    A_rad = np.zeros((_n, _n))
    for i in range(_n):
        for j in range(_n):
            A_med[i,j] = (A[i][j].upper + A[i][j].lower) / 2
            A_rad[i,j] = A[i][j].upper - A[i][j].lower

    max_eig_val = -1
    if (abs(la.det(A_med)) < 1e-7):
        return False, max_eig_val
    else:
        A_med_inv = abs(la.inv(A_med))
        buf_mat = np.matmul(A_med_inv, A_rad)
        eig_val = la.eigvals(buf_mat)
        max_eig_val = max(abs(eig_val))
    if (max_eig_val < 1):
        return True, max_eig_val
    else:
        return False, max_eig_val

def diag_max_criteria(A):
    _n = len(A)
    A_med = np.zeros((_n, _n))
    A_rad = np.zeros((_n, _n))
    for i in range(_n):
        for j in range(_n):
            A_med[i,j] = (A[i][j].upper + A[i][j].lower) / 2
            A_rad[i,j] = A[i][j].upper - A[i][j].lower

    max_diag_val = -1
    if (abs(la.det(A_med)) < 1e-7):
        return False, max_diag_val
    else:
        A_med_inv = abs(la.inv(A_med))
        buf_mat = np.matmul(A_rad, A_med_inv)
        diag_val = buf_mat.diagonal()
        max_diag_val = max(abs(diag_val))
    if (max_diag_val >= 1):
        return True, max_diag_val
    else:
        return False, max_diag_val


def rump_criteria(A):
    _n = len(A)
    A_med = np.zeros((_n, _n))
    A_rad = np.zeros((_n, _n))
    for i in range(_n):
        for j in range(_n):
            A_med[i,j] = (A[i][j].upper + A[i][j].lower) / 2
            A_rad[i,j] = A[i][j].upper - A[i][j].lower

    eig_val_rad = la.eigvals(A_rad)
    eig_val_med = la.eigvals(A_med)
    max_eig_val_rad = max(eig_val_rad)
    min_eig_val_med = min(eig_val_med)

    if (max_eig_val_rad < min_eig_val_med):
        return True, max_eig_val_rad, min_eig_val_med
    else:
        return False, max_eig_val_rad, min_eig_val_med



def make_matrix(_n, _eps):
    A = []
    len(A)
    for i in range(_n):
        _a = []
        for j in range(_n):
            if i == j:
                _a.append(interval(1, 1))
            else:
                _a.append(interval(0, _eps))
        A.append(_a)
    return A


eps = [0, 1 / 70, 1/42, 1/41, 1/40, 1]

print("Task 1")
for e in eps:
    print("eps =", e)
    print("det =", count_interval_det_2x2_matrix(e))
    print()
print()

print("Task 2")

sizes = [*range(2, 21)]
eps_step = 1e-3

for n in sizes:
    print("n = ", n)
    print ("1 / (n - 1) = ", 1 / (n - 1))
    eps = eps_step
    A = make_matrix(n, eps)

    beck_criteria_vals = beck_criteria(A)
    rump_criteria_vals = rump_criteria(A)
    while (beck_criteria_vals[0] == True or rump_criteria_vals[0] == True):
        eps += eps_step
        A = make_matrix(n, eps)
        beck_criteria_vals = beck_criteria(A)
        rump_criteria_vals = rump_criteria(A)
    eps -= eps_step
    A = make_matrix(n, eps)
    beck_criteria_vals = beck_criteria(A)
    rump_criteria_vals = rump_criteria(A)
    print("Last non-special matrix with eps: ", eps)
    print("Beck criteria: ", beck_criteria_vals)
    print("Rump criteria: ", rump_criteria_vals)

    ##eps = 1 / (n - 1)
    ##A = make_matrix(n, eps)
    ##diag_max_criteria_vals = diag_max_criteria(A)
    ##while (diag_max_criteria_vals[0] == False):
    ##    eps += eps_step
    ##    A = make_matrix(n, eps)
    ##    diag_max_criteria_vals = diag_max_criteria(A)
    ##print("First special matrix with eps: ", eps)
    ##print("Max diag criteria: ", diag_max_criteria_vals)

    print()

