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


def generateNumbers():
    startInterval = -(math.pi / 2)
    endInterval = math.pi / 2

    x = np.random.uniform(startInterval, endInterval, 10000)
    return x


def hierarchyTan(tanDict):
    tanDict = dict(sorted(tanDict.items(), key=lambda item: item[1], reverse=True))

    place = 1
    print("The hierachy of the Tangent:")
    for i in tanDict.keys():
        print(f"{place}. T{i}")
        place += 1

def countErrors(listOfNumbers):
    errorDict = {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in range(len(listOfNumbers)):
        a = listOfNumbers[i]

        pyTan = math.tan(a)

        aproxTan4 = T4(a)
        aproxTan5 = T5(a)
        aproxTan6 = T6(a)
        aproxTan7 = T7(a)
        aproxTan8 = T8(a)
        aproxTan9 = T9(a)

        errors = {
            4: abs(aproxTan4 - pyTan),
            5: abs(aproxTan5 - pyTan),
            6: abs(aproxTan6 - pyTan),
            7: abs(aproxTan7 - pyTan),
            8: abs(aproxTan8 - pyTan),
            9: abs(aproxTan9 - pyTan)
        }

        for key in errorDict.keys():
            errorDict[key] += errors[key]

    return errorDict

def hierarchyApproximations(listOfNumbers):
    approximations = {4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

    for a in listOfNumbers:
        errors = {
            4: abs(T4(a) - math.tan(a)),
            5: abs(T5(a) - math.tan(a)),
            6: abs(T6(a) - math.tan(a)),
            7: abs(T7(a) - math.tan(a)),
            8: abs(T8(a) - math.tan(a)),
            9: abs(T9(a) - math.tan(a))
        }

        lista_sorted = sorted(errors.items(), key=lambda x: x[1])
        first_three_min_errors = lista_sorted[:3]

        for key, _ in first_three_min_errors:
            approximations[key].append(a)


        print(f"Number {a}:")
        for tuple in first_three_min_errors:
            print(f"    T{tuple[0]}")



    return approximations


def main():
    listOfNumbers = generateNumbers()
    print(f"Verify if they are really 10000 numbers: {len(listOfNumbers)}")

    bestTanDict = {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in range(0, len(listOfNumbers)):
        a = listOfNumbers[i]

        pyTan = math.tan(a)

        aproxTan4 = T4(a)
        aproxTan5 = T5(a)
        aproxTan6 = T6(a)
        aproxTan7 = T7(a)
        aproxTan8 = T8(a)
        aproxTan9 = T9(a)

        betterIndex = 4
        betterValue = abs(aproxTan4 - pyTan)

        if betterValue > abs(aproxTan5 - pyTan):
            betterIndex = 5
            betterValue = abs(aproxTan5 - pyTan)

        if betterValue > abs(aproxTan6 - pyTan):
            betterIndex = 6
            betterValue = abs(aproxTan6 - pyTan)

        if betterValue > abs(aproxTan7 - pyTan):
            betterIndex = 7
            betterValue = abs(aproxTan7 - pyTan)

        if betterValue > abs(aproxTan8 - pyTan):
            betterIndex = 8
            betterValue = abs(aproxTan8 - pyTan)

        if betterValue > abs(aproxTan9 - pyTan):
            betterIndex = 9

        bestTanDict[betterIndex] += 1

    hierarchyTan(bestTanDict)

    errorDict = countErrors(listOfNumbers)

    print("\nNumber of errors for each approximation:")
    for key, value in errorDict.items():
        print(f"T{key}: {value}")

    print("Hierarchy of approximations for each generated number:")

    approximations = hierarchyApproximations(listOfNumbers)


if __name__ == '__main__':
    main()
