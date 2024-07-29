import numpy as np
import math

def T4(a):
    result = 105 * a - 10 * pow(a, 3)
    result = result / (105 - 45 * pow(a, 2) + pow(a, 4))
    return result


def T5(a):
    result = 945 * a - 105 * pow(a, 3) + pow(a, 5)
    result = result / (945 - 420 * pow(a, 2) + 15 * pow(a, 4))
    return result


def T6(a):
    result = 10395 * a - 1260 * pow(a, 3) + 21 * pow(a, 5)
    result = result / (10395 - 4725 * pow(a, 2) + 210 * pow(a, 4) - pow(a, 6))
    return result


def T7(a):
    result = 135135 * a - 17325 * pow(a, 3) + 378 * pow(a, 5) - pow(a, 7)
    result = result / (135135 - 62370 * pow(a, 2) + 3150 * pow(a, 4) - 28 * pow(a, 6))
    return result


def T8(a):
    result = 2027025 * a - 270270 * pow(a, 3) + 6930 * pow(a, 5) - 36 * pow(a, 7)
    result = result / (2027025 - 945945 * pow(a, 2) + 51975 * pow(a, 4) - 630 * pow(a, 6) + pow(a, 8))
    return result


def T9(a):
    result = 34459425 * a - 4729725 * pow(a, 3) + 135135 * pow(a, 5) - 990 * pow(a, 7) + pow(a, 9)
    result = result / (34459425 - 16216200 * pow(a, 2) + 945945 * pow(a, 4) - 13860 * pow(a, 6) + 45 * pow(a, 8))
    return result

def S4(a):
    result = T4(a) / math.sqrt(1 + T4(a) ** 2)
    return result
def S5(a):
    result = T5(a) / math.sqrt(1 + T5(a) ** 2)
    return result
def S6(a):
    result = T6(a)/math.sqrt(1+T6(a)**2)
    return result
def S7(a):
    result = T7(a) / math.sqrt(1 + T7(a) ** 2)
    return result

def S8(a):
    result = T8(a) / math.sqrt(1 + T8(a) ** 2)
    return result
def S9(a):
    result = T9(a) / math.sqrt(1 + T9(a) ** 2)
    return result

def C6(a):
    result = 1/math.sqrt(1+T6(a)**2)
    return result
def C7(a):
    result = 1 / math.sqrt(1 + T7(a) ** 2)
    return result


def C4(a):
    result = 1/math.sqrt(1+T4(a)**2)
    return result
def C5(a):
    result = 1 / math.sqrt(1 + T5(a) ** 2)
    return result

def C8(a):
    result = 1/math.sqrt(1+T8(a)**2)
    return result
def C9(a):
    result = 1 / math.sqrt(1 + T9(a) ** 2)
    return result




def generateNumbers():
    startInterval = -(math.pi / 2)
    endInterval = math.pi / 2

    x = np.random.uniform(startInterval, endInterval, 10000)
    return x


def hierarchySin(sinDict):
    sinDict = dict(sorted(sinDict.items(), key=lambda item: item[1], reverse=True))

    place = 1
    print("The hierachy of the Sinus:")
    for i in sinDict.keys():
        print(f"{place}. S{i}")
        place += 1

def hierarchyCos(cosDict):
    cosDict = dict(sorted(cosDict.items(), key=lambda item: item[1], reverse=True))

    place = 1
    print("The hierachy of the Cosinus:")
    for i in cosDict.keys():
        print(f"{place}. C{i}")
        place += 1

def hierarchyApproximationsSin(listOfNumbers):
    approximations = {4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for a in listOfNumbers:
        errors = {
            4: abs(S4(a) - math.sin(a)),
            5: abs(S5(a) - math.sin(a)),
            6: abs(S6(a) - math.sin(a)),
            7: abs(S7(a) - math.sin(a)),
            8: abs(S8(a) - math.sin(a)),
            9: abs(S9(a) - math.sin(a))
        }

        lista_sorted = sorted(errors.items(), key=lambda x: x[1])
        first_three_min_errors = lista_sorted[:3]

        for key, _ in first_three_min_errors:
            approximations[key].append(a)


        print(f"Number {a}:")
        for tuple in first_three_min_errors:
            print(f"    S{tuple[0]}")



    return approximations

def hierarchyApproximationsCos(listOfNumbers):
    approximations = {4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for a in listOfNumbers:
        errors = {
            4: abs(C4(a) - math.cos(a)),
            5: abs(C5(a) - math.cos(a)),
            6: abs(C6(a) - math.cos(a)),
            7: abs(C7(a) - math.cos(a)),
            8: abs(C8(a) - math.cos(a)),
            9: abs(C9(a) - math.cos(a))
        }

        lista_sorted = sorted(errors.items(), key=lambda x: x[1])
        first_three_min_errors = lista_sorted[:3]

        for key, _ in first_three_min_errors:
            approximations[key].append(a)


        print(f"Number {a}:")
        for tuple in first_three_min_errors:
            print(f"    C{tuple[0]}")



    return approximations


def main():
    listOfNumbers = generateNumbers()
    print(f"Verify if they are really 10000 numbers: {len(listOfNumbers)}")

    bestSinDict = {4:0, 5:0,6: 0,  7: 0,8:0, 9:0}
    bestCosDict = {4:0, 5:0,6: 0,  7: 0,8:0, 9:0}

    for i in range(0, len(listOfNumbers)):
        a = listOfNumbers[i]

        pySin = math.sin(a);

        aproxSin4 = S4(a)
        aproxSin5 = S5(a)
        aproxSin6 = S6(a)
        aproxSin7 = S7(a)
        aproxSin8 = S8(a)
        aproxSin9 = S9(a)

        betterIndex = 4
        betterValue = abs(aproxSin4 - pySin)


        if betterValue > abs(aproxSin5 - pySin):
            betterIndex = 5
            betterValue = abs(aproxSin5 - pySin)

        if betterValue > abs(aproxSin6 - pySin):
            betterIndex = 6
            betterValue = abs(aproxSin6 - pySin)

        if betterValue > abs(aproxSin7 - pySin):
            betterIndex = 7
            betterValue = abs(aproxSin7 - pySin)

        if betterValue > abs(aproxSin8 - pySin):
            betterIndex = 8
            betterValue = abs(aproxSin8 - pySin)

        if betterValue > abs(aproxSin9 - pySin):
            betterIndex = 9


        bestSinDict[betterIndex] += 1

    hierarchySin(bestSinDict)

    for i in range(0, len(listOfNumbers)):
        a = listOfNumbers[i]

        pyCos = math.cos(a)

        aproxCos4 = C4(a)
        aproxCos5 = C5(a)
        aproxCos6 = C6(a)
        aproxCos7 = C7(a)
        aproxCos8 = C8(a)
        aproxCos9 = C9(a)

        betterIndex = 4
        betterValue = abs(aproxCos4 - pyCos)

        if betterValue > abs(aproxCos5 - pyCos):
            betterIndex = 5
            betterValue = abs(aproxCos5 - pyCos)

        if betterValue > abs(aproxCos6 - pyCos):
            betterIndex = 6
            betterValue = abs(aproxCos6 - pyCos)

        if betterValue > abs(aproxCos7 - pyCos):
            betterIndex = 7
            betterValue = abs(aproxCos7 - pyCos)

        if betterValue > abs(aproxCos8 - pyCos):
            betterIndex = 8
            betterValue = abs(aproxCos8 - pyCos)

        if betterValue > abs(aproxCos9 - pyCos):
            betterIndex = 9

        bestCosDict[betterIndex] += 1
    hierarchyCos(bestCosDict)

    print("Hierarchy of approximations of Sinus for each generated number:")
    hierarchyApproximationsSin(listOfNumbers)

    print("Hierarchy of approximations of Cosinus for each generated number:")
    hierarchyApproximationsCos(listOfNumbers)


if __name__ == '__main__':
    main()

