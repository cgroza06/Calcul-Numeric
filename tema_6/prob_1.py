import numpy as np
import math

def func(x):
    return x**4 - 12*x**3 + 30*x**2 + 12

def least_squares(n, m, x0, xn):
    h = (xn - x0) / n
    points = [(x0, func(x0))]

    for i in range(1, n):
        points.append((x0 + i * h, func(x0 + i * h)))

    points.append((xn, func(xn)))

    B = np.array([[sum([point[0] ** (i + j) for point in points])
            for j in range(0, m + 1)] for i in range(0, m + 1)])
    f = np.array([sum([point[1] * (point[0] ** i) for point in points])
            for i in range(0, m + 1)])
    a = np.linalg.solve(B, f)

    sum_abs_diff = sum([math.fabs(schema_horner(a, point[0]) - point[1]) for point in points])

    return sum_abs_diff, a


def schema_horner(c, x):
    n = len(c)
    d = c[n - 1]
    for i in range(n - 2, -1, -1):
        d = c[i] + d * x
    return d



def calcul_delta_y(y):
    n = len(y)
    table = [y]
    for j in range(1, n):
        next_row = []
        for i in range(n - j):
            next_row.append(table[j - 1][i + 1] - table[j - 1][i])
        table.append(next_row)
        y[j]=next_row[0]
    return y

def calcul_s(t, k):
    if k == 1:
        return t
    else:
        return calcul_s(t, k - 1) * ((t - k + 1) / k)

def main():
    n_e = 5
    h_e=1
    x_exemplu = [0, 1, 2, 3, 4, 5]
    y_exemplu = [50, 47, -2, -121, -310, -545]

    delta_y_e = calcul_delta_y(y_exemplu)
    x_final_exemplu = 1.5
    t_exemplu = (x_final_exemplu - x_exemplu[0]) / h_e
    s_e = [calcul_s(t_exemplu, k) for k in range(1, n_e + 1)]
    result_e = y_exemplu[0]
    for k in range(1, n_e):
        result_e += delta_y_e[k] * s_e[k - 1]

    print(f"Exemplu 1: {x_final_exemplu} este: {result_e}")


    n = int(input("Introduceți n: "))
    x = [0] * (n + 1)
    x[0], x[n] = map(int, input("Introduceți  x0 și xn, separate prin spațiu: ").split())
    h = (x[n] - x[0]) / n

    for i in range(1, n):
        x[i] = x[0] + i * h

    y = [0] * (n + 1)
    for i in range(0, n + 1):
        y[i] = func(x[i])
    delta_y = calcul_delta_y(y)


    x_final = float(input("Introduceți x_final: "))
    t = (x_final - x[0]) / h
    s = [calcul_s(t, k) for k in range(1, n+1)]
    result = y[0]
    for k in range(1, n):
        result += delta_y[k] * s[k-1]


    print(f"L_n({x_final}) este: {result}")

    functia = func(x_final)
    print (f"Valoarea functiei in punctul {x_final} este: {functia}")
    print(f"L_n({x_final})-f({x_final}):{math.fabs(result-functia)}")

    m = int(input("Introduceți m: "))
    suma_dif, c = least_squares(n, m, x[0], x[n])
    horner = schema_horner(c, x_final)

    print(f'x = {x_final}')
    print(f'f(x) = {functia}')
    print(f'Pm(x) = {horner}')
    print(f'|Pm(x) - f(x)| = {math.fabs(horner - functia)}')
    print (f'Suma Pm(x_i)-y_i , i apartine [0,n]: {suma_dif}')


if __name__ == "__main__":
    main()