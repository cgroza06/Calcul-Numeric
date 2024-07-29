import numpy as np
import math

epsilon = None

def generate_random_matrix(size):
    return np.random.rand(size, size) * 10

def descompunerea_LU_in_A(A_init):
    n = len(A_init)
    A = np.zeros((n, n))
    for p in range(n):
        for i in range(p, n):
            suma = sum(A[i, k] * A[k, p] for k in range(p))
            A[i, p] = A_init[i, p] - suma
        for i in range(p + 1, n):
            suma = sum(A[p, k] * A[k, i] for k in range(p))
            if math.fabs(A[p, p]) <= epsilon:
                print("Nu se poate calcula descompunerea LU")
                exit(0)
            else:
                A[p, i] = (A_init[p, i] - suma) / A[p, p]

    return A

def determinant_A(A):
    n = len(A)
    det = 1.0

    for i in range(n):
        if A[i][i] == 0:
            return 0
        det = det * A[i][i]
    return det

def substitutie_inferioara(A, b):
    n = len(A)
    y = np.zeros(n)

    for i in range(n):
        y[i] = b[i] - sum(A[i][j] * y[j] for j in range(i))
        y[i] /= A[i][i]

    return y

def substitutie_superioara(A, y):
    n = len(A)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x

def norma(A_init, b_init, x_aprox):
    suma = 0
    dif = np.dot(A_init, x_aprox) - b_init
    for i in range(len(dif)):
        suma += (dif[i] * dif[i])

    return np.sqrt(suma)

def print_results(A, A_init, b_init, x_aprox, x_exact, A_inv):
    print("\nMatricea A după descompunerea LU:")
    print(A)
    print(f"\nDeterminantul matricii A este: {determinant_A(A):.10f}")
    print(f"\nSoluția aproximativă a sistemului Ax = b este: {x_aprox}")
    print(f"\nNorma = {norma(A_init, b_init, x_aprox)}")
    print(f"\nSolutia exacta a sistemului Ax = b este: {x_exact}")
    print(f"\nInversa matricii A este:\n{A_inv}")
    norma1 = np.linalg.norm(x_aprox - x_exact)
    norma2 = np.linalg.norm(x_aprox - np.dot(A_inv, b_init))
    print(f"\nNorma1: {norma1}")
    print(f"Norma2: {norma2}")

def main():
    global epsilon
    input_epsilon = int(input("Putere pentru epsilon:"))
    epsilon = 10 **(-input_epsilon)
    size=int(input("Dimensiunea matricii:"))
    A_init = generate_random_matrix(size)
    b_init = np.random.rand(size) * 10
    print("\nDimensiunea matricii generate random:", size)
    print("\nMatricea A generată random:")
    print(A_init)
    print("\nVectorul termenilor liberi generat random:")
    print(b_init)

    A = descompunerea_LU_in_A(A_init)

    y = substitutie_inferioara(A, b_init)
    x_aprox = substitutie_superioara(A, y)

    x_exact = np.linalg.solve(A_init, b_init)
    A_inv = np.linalg.inv(A_init)

    print_results(A, A_init, b_init, x_aprox, x_exact, A_inv)

    print("\n------------------Exemplu din fișier----------------")
    A = np.array([[2.5, 2, 2],
                  [5, 6, 5],
                  [5, 6, 6.5]])
    b = np.array([2, 2, 2])

    A_init = A.copy()
    b_init = b.copy()

    A = descompunerea_LU_in_A(A_init)

    y = substitutie_inferioara(A, b_init)
    x_aprox = substitutie_superioara(A, y)

    x_exact = np.linalg.solve(A_init, b_init)

    A_inv = np.linalg.inv(A_init)

    print_results(A, A_init, b_init, x_aprox, x_exact, A_inv)

if __name__ == "__main__":
    main()
