import math
import numpy as np

epsilon = None
k_max = 10000


def norma2(b, matrice, coloane, x):
    dimensiune = len(matrice)
    results = [0] * dimensiune
    norme = [0] * dimensiune
    for i in range(dimensiune):
        for index, valoare in enumerate(matrice[i]):
            results[i] += valoare * x[coloane[i][index]]
        norme[i]=results[i]-b[i]
    return np.linalg.norm(norme)

def metoda2(b, matrice, coloane):
    dimensiune = len(matrice)
    x = [0] * dimensiune
    k = 0
    norma_totala = 1000
    while norma_totala>=epsilon and k<=k_max and norma_totala<=10**8:
        norma_totala = 0
        for i in range(dimensiune):
            suma = 0
            val_diag = None
            for index, valoare in enumerate(matrice[i]):
                if coloane[i][index]!=i:
                    suma+= valoare*x[coloane[i][index]]
                else:
                    val_diag = valoare

            aux = x[i]

            x[i] = (b[i] - suma)/val_diag
            norma = (x[i] - aux)**2

            norma_totala+=norma
        norma_totala = math.sqrt(norma_totala)

        k = k + 1
    if norma_totala < epsilon:
        return k, x
    else:
        print("Divergență.")
        return None

def norma1(b, matrice, x):
    dimensiune = len(matrice)
    results = [0] * dimensiune
    norme = [0] * dimensiune
    for i in range(dimensiune):

        for valoare, coloana in matrice[i]:
            results[i]+=valoare * x[coloana]
        norme[i]=results[i]-b[i]
    return np.linalg.norm(norme)

def metoda1(b , matrice):
    dimensiune = len(matrice)
    x = [0] * dimensiune
    k=0
    norma_totala = 1000

    while norma_totala>=epsilon and k<=k_max and norma_totala<=10**8:
        norma_totala = 0
        for i in range(dimensiune):
            suma = 0
            val_diag = None
            for valoare, coloana in matrice[i]:
                if coloana!=i:
                    suma += valoare * x[coloana]
                else:
                    val_diag = valoare
            aux = x[i]

            x[i] = (b[i] - suma)/val_diag
            norma = (x[i] - aux)**2

            norma_totala+=norma
        norma_totala = math.sqrt(norma_totala)

        k = k + 1
    if norma_totala < epsilon:
        return k, x
    else:
        print("Divergență.")
        return None


def citeste_vector_termeni_liberi(nume_fisier):
    vector_termeni_liberi = []
    with open(nume_fisier, 'r') as f:
        dimensiune_vector = int(f.readline().strip())
        for linie in f:
            linie_curata = linie.strip()
            if linie_curata:  # Verificăm dacă linia nu este goală
                valoare = float(linie_curata)
                vector_termeni_liberi.append(valoare)
    return vector_termeni_liberi

def suma2(a, b, dim):
    a_plus_b = [None] * dim
    for i in range(dim):
        a_plus_b[i] = []

        j_a = 0
        j_b = 0

        while j_a < len(a[i]) and j_b < len(b[i]):
            if a[i][j_a][1] == b[i][j_b][1]:
                suma = a[i][j_a][0] + b[i][j_b][0]
                if suma != 0:
                    a_plus_b[i].append((suma, a[i][j_a][1]))
                j_a += 1
                j_b += 1
            elif a[i][j_a][1] < b[i][j_b][1]:
                a_plus_b[i].append((a[i][j_a][0], a[i][j_a][1]))
                j_a += 1
            else:
                a_plus_b[i].append((b[i][j_b][0], b[i][j_b][1]))
                j_b += 1

        while j_a < len(a[i]):
            a_plus_b[i].append((a[i][j_a][0], a[i][j_a][1]))
            j_a += 1

        while j_b < len(b[i]):
            a_plus_b[i].append((b[i][j_b][0], b[i][j_b][1]))
            j_b += 1

    return a_plus_b


def memorare_rara_pentru_suma(nume_fisier):
    with open(nume_fisier, 'r') as f:
        dimensiune_matrice = int(f.readline().strip())
        matrice_rara = [None] * dimensiune_matrice
        for linie in f:
            if linie.strip():
                # Splităm linia în valorile separate
                valori = linie.strip().split(',')
                # Prima valoare este cheia
                cheie = float(valori[0])
                # Valorile următoare sunt tuplul (i, j)
                i, j = map(int, valori[1:])
                if matrice_rara[i] is None:
                    matrice_rara[i] = [(cheie, j)]  # Dacă nu există, creăm o nouă listă cu tuplul (cheie, j)
                else:
                    found = False
                    for index, (suma, coloana) in enumerate(matrice_rara[i]):
                        if coloana == j:
                            matrice_rara[i][index] = (suma + cheie, coloana)
                            found = True
                            break
                    if not found:
                        matrice_rara[i].append((cheie, j))
        for linie in matrice_rara:
            if linie is not None:
                linie.sort(key=lambda x: x[1])

        return matrice_rara, dimensiune_matrice


def metoda_1_de_memorare_rara(nume_fisier):
    with open(nume_fisier, 'r') as f:
        dimensiune_matrice = int(f.readline().strip())
        matrice_rara = [None] * dimensiune_matrice
        has_zero_on_diagonal = False
        for linie in f:
            if linie.strip():
                # Splităm linia în valorile separate
                valori = linie.strip().split(',')
                # Prima valoare este cheia
                cheie = float(valori[0])
                # Valorile următoare sunt tuplul (i, j)
                i, j = map(int, valori[1:])
                if i == j and math.fabs(cheie) <= epsilon:
                    # Dacă elementul este pe diagonala și este zero
                    has_zero_on_diagonal = True
                if matrice_rara[i] is None:
                    matrice_rara[i] = [(cheie, j)]  # Dacă nu există, creăm o nouă listă cu tuplul (cheie, j)
                else:
                    found = False
                    for index, (suma, coloana) in enumerate(matrice_rara[i]):
                        if coloana == j:
                            matrice_rara[i][index] = (suma + cheie, coloana)
                            found = True
                            break
                    if not found:
                        matrice_rara[i].append((cheie, j))
        if has_zero_on_diagonal:
            print("Nu se poate rezolva sistemul deoarece avem 0 pe diagonala")
            return None  # Returnăm None dacă există elemente nule pe diagonala
        else:
            return matrice_rara


def verify_equality(matrix1, matrix2):
    # Verificăm dacă dimensiunile matricelor sunt egale
    if len(matrix1) != len(matrix2):
        return False

    for i in range(len(matrix1)):
        # Verificăm dacă dimensiunea fiecărui rând al fiecărei matrici este aceeași
        if len(matrix1[i]) != len(matrix2[i]):
            return False

        for j in range(len(matrix1[i])):
            # Verificăm fiecare element al matricelor
            if math.fabs(matrix1[i][j][0] - matrix2[i][j][0]) >= epsilon:
                return False
    return True


def metoda_2_de_memorare_rara(nume_fisier):
    with open(nume_fisier, 'r') as f:
        dimensiune_matrice = int(f.readline().strip())
        valori = [[] for _ in range(dimensiune_matrice)]  # Inițializăm lista de liste pentru valorile matricei rare
        ind_col = [[] for _ in range(dimensiune_matrice)]  # Inițializăm lista de liste pentru indicii de coloană
        has_zero_on_diagonal = False
        for linie in f:
            if linie.strip():
                # Splităm linia în valorile separate
                cheie, i, j = map(float, linie.strip().split(','))
                i, j = int(i), int(j)
                if i == j and math.fabs(cheie) <= epsilon:
                    # Dacă elementul este pe diagonala și este zero
                    has_zero_on_diagonal = True
                valori[i].append(cheie)
                ind_col[i].append(int(j))
        if has_zero_on_diagonal:
            print("Nu se poate rezolva sistemul deoarece avem 0 pe diagonala")
            return None, None  # Returnăm None dacă există elemente nule pe diagonala
        else:
            # Afisarea matricei rare după metoda de memorare
            print("valori =", valori)
            print("ind_col =", ind_col)
            return valori, ind_col


def main():
    global epsilon
    input_epsilon = int(input("Putere pentru epsilon:"))
    epsilon = 10 ** (-input_epsilon)
    while True:
        print("1. Citeste din a1.txt")
        print("2. Citeste din a2.txt")
        print("3. Citeste din a3.txt")
        print("4. Citeste din a4.txt")
        print("5. Citeste din a5.txt")
        print("6. Citeste din a6.txt")
        print("7. Citeste din a7.txt")
        print("8. Citeste din a.txt si b.txt")
        print("9. Iesire")
        optiune = input("Selecteaza optiunea: ")

        if optiune == "9":
            break
        elif optiune in ["1", "2", "3", "4", "5", "6", "7","8","9"]:
            if(optiune == "8"):
                nume_fisier_a = f'data set {optiune}/a_{optiune}.txt'
                nume_fisier_b = f'data set {optiune}/b_{optiune}.txt'
                nume_fisier_a_plus_b =f'data set 8/aplusb.txt'
            else:
                nume_fisier_a = f'data set {optiune}/a_{optiune}.txt'
                nume_fisier_b = f'data set {optiune}/b_{optiune}.txt'

            print("Alege o metoda de memorare rara:")
            print("1. Metoda 1")
            print("2. Metoda 2")
            print("3. Bonus")
            optiune_memorare = input("Selecteaza optiunea de memorare rara: ")

            if optiune_memorare == "1":
                matrice = metoda_1_de_memorare_rara(nume_fisier_a)
                vector = citeste_vector_termeni_liberi(nume_fisier_b)
                if matrice is not None and vector is not None:

                    print("Matricea rara este:")
                    for i in range(len(matrice)):
                        print(f"Linia {i}: {matrice[i]}")
                    if (metoda1(vector, matrice) == None):
                        continue
                    k, x = metoda1(vector, matrice)
                    norma_ex_3 = norma1(vector, matrice, x)
                    print(f"Soluția:{x}")
                    print(f"Convergența realizată în {k + 1} iterații.")
                    print(f"Norma: {norma_ex_3}")
            elif optiune_memorare == "2":
                matrice, coloane = metoda_2_de_memorare_rara(nume_fisier_a)
                vector = citeste_vector_termeni_liberi(nume_fisier_b)
                if(metoda2(vector, matrice, coloane)==None):
                    continue
                k, x = metoda2(vector, matrice, coloane)
                norma_ex_3_2 = norma2(vector, matrice, coloane, x)
                print(f"Soluția:{x}")
                print(f"Convergența realizată în {k + 1} iterații.")
                print(f"Norma : {norma_ex_3_2}")
            elif optiune_memorare=="3":
                matrice_a, dim_a=memorare_rara_pentru_suma(nume_fisier_a)
                matrice_b, dim_b=memorare_rara_pentru_suma(nume_fisier_b)
                matrice_a_plus_b, dim_aplusb = memorare_rara_pentru_suma(nume_fisier_a_plus_b)
                m_b=metoda_1_de_memorare_rara(nume_fisier_b)

                matrice_suma = suma2(matrice_a, matrice_b,dim_a)


                if verify_equality(matrice_suma, matrice_a_plus_b) == True:
                    print("sunt egale")
                else:
                    print("nu sunt egale")



            else:
                print("Optiune invalida pentru metoda de memorare rara.")
                continue

        else:
            print("Optiune invalida! Selecteaza din nou.")


if __name__ == "__main__":
    main()
