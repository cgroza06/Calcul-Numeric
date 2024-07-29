import numpy as np
import math


def calculate_I_n(n):
    I_n = np.eye(n)
    return I_n


def factorization_QR(b_init, A_init):
    A = A_init.copy()
    b = b_init.copy()
    n = len(b)
    u = np.zeros(n)
    q = calculate_I_n(n)

    for r in range(n - 1):
        # Constructia matricii P_r matrix
        teta = sum(A[i, r] ** 2 for i in range(r, n))
        if teta <= epsilon:
            continue
        k = math.sqrt(teta)
        if A[r, r] > 0:
            k = -k
        beta = teta - k * A[r, r]
        u[r] = A[r, r] - k

        for i in range(r + 1, n):
            u[i] = A[i, r]

        # Transformarea coloanelor j
        for j in range(r + 1, n):
            suma = sum(u[i] * A[i, j] for i in range(r, n))
            gama = suma / beta
            for i in range(r, n):
                A[i, j] -= gama * u[i]

        # Transformarea coloanelor r a matricii A
        A[r, r] = k
        for i in range(r + 1, n):
            A[i, r] = 0

        suma = sum(u[i] * b[i] for i in range(r, n))
        gama = suma / beta

        for i in range(r, n):
            b[i] -= gama * u[i]

        for j in range(n):
            suma = sum(u[i] * q[i, j] for i in range(r, n))
            gama = suma / beta
            for i in range(r, n):
                q[i, j] -= gama * u[i]

    return b, A, q


def generate_random_vector(size):
    return np.random.rand(size) * 10


def generate_random_matrix(size):
    return np.random.rand(size, size) * 10


def calculate_vector_b(s, A):
    n = len(s)
    b = np.zeros(n)
    for i in range(n):
        suma = 0
        for j in range(n):
            suma += s[j]*A[i, j]
        b[i] = suma

    return b


def solve_system(A, b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if math.fabs(A[i,i]) <= epsilon:
            return None
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x


def solve_linear_system_with_qr(A, b):
    Q, R = np.linalg.qr(A)
    b_modified = np.dot(Q.T, b)
    x = np.linalg.solve(R, b_modified)
    return x


def calculate_inverse_using_QR(A_init, Q, R):
    A = A_init.copy()
    n = len(A)
    if np.abs(np.linalg.det(A)) < epsilon:
        print("Matricea este singulară. Inversa nu poate fi calculată.")
        return None
    A_inv = np.zeros((n, n))
    for j in range(n):
        b = Q.T[:, j]
        x = solve_system(R, b)
        A_inv[:, j] = x
    return A_inv


def calculate_norma(x, y):
    return np.linalg.norm(x - y)


def print_result(Q_t, A, x_householder, x_library, norm, error_1, error_2, error_3, error_4, norm_difference):

    print(f"Q = \n{Q_t.T}")
    print(f"R = \n{A}")
    print(f"Solutia, folosind metoda Householder: {x_householder}")
    print(f"Solutia folosind descompunerea QR: {x_library}")
    print(f"Norma: {norm}")
    print(f"Error 1: {error_1}")
    print(f"Error 2: {error_2}")
    print(f"Error 3: {error_3}")
    print(f"Error 4: {error_4}")
    print("Norma: Diferenta dintre A_Householder^(-1) si A_bibl^(-1):", norm_difference)


def main():
    global epsilon
    input_epsilon = int(input("Introduceti puterea lui Epsilon: "))
    epsilon = 10 ** (-input_epsilon)
    size = int(input("Introduceti dimensiunea matricii: "))

    A_init = generate_random_matrix(size)
    for i in range(size):
        A_init[0,i]=A_init[1,i]
    s_init = generate_random_vector(size)
    print(f"Matricea generata A:\n{A_init}")

    b_init = calculate_vector_b(s_init, A_init)
    print(f"Vectorul b:{b_init}")

    b, A, Q_t = factorization_QR(b_init, A_init)
    R = A
    Q = Q_t.T

    x_householder = solve_system(A, b)
    x_library = solve_linear_system_with_qr(A_init, b_init)
    if x_householder is None:
        print("Operatiile cu aceasta matrice nu pot fi efectuate ")

    else:

        norm = calculate_norma(x_library, x_householder)
        error_1 = calculate_norma(np.dot(A_init, x_householder), b_init)
        error_2 = calculate_norma(np.dot(A_init, x_library), b_init)
        error_3 = calculate_norma(x_householder, s_init) / calculate_norma(s_init, np.zeros(len(s_init)))
        error_4 = calculate_norma(x_library, s_init) / calculate_norma(s_init, np.zeros(len(s_init)))

        A_Householder_inv = calculate_inverse_using_QR(A_init, Q, R)
        A_bibl_inv = np.linalg.inv(A_init)
        norm_difference = calculate_norma(A_Householder_inv, A_bibl_inv)

        print_result(Q_t, A, x_householder, x_library, norm, error_1, error_2, error_3, error_4, norm_difference)

    print("\n------------------Exemplu din fisier----------------")

    A_example = np.array([[0, 0, 4],
                          [1, 2, 3],
                          [0, 1, 2]])
    s_example = np.array([3, 2, 1])
    b_example = calculate_vector_b(s_example, A_example)
    print(f"Vectorul b:{b_example}")

    b, A, Q_t = factorization_QR(b_example, A_example)
    R = A
    Q = Q_t.T

    x_householder = solve_system(A, b)

    x_library = solve_linear_system_with_qr(A_example, b_example)

    norm = calculate_norma(x_library, x_householder)

    error_1 = calculate_norma(np.dot(A_example, x_householder), b_example)
    error_2 = calculate_norma(np.dot(A_example, x_library), b_example)
    error_3 = calculate_norma(x_householder, s_example) / calculate_norma(s_example, np.zeros(len(s_example)))
    error_4 = calculate_norma(x_library, s_example) / calculate_norma(s_example, np.zeros(len(s_example)))

    A_Householder_inv = calculate_inverse_using_QR(A_example, Q, R)

    A_bibl_inv = np.linalg.inv(A_example)

    norm_difference = calculate_norma(A_Householder_inv, A_bibl_inv)

    print_result(Q_t, A, x_householder, x_library, norm, error_1, error_2, error_3, error_4, norm_difference)


if __name__ == "__main__":
    main()
