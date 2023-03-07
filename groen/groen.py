import math


def main():
    numTests = int(input())
    for test in range(numTests):
        runTest(str(test+1))


def runTest(testNr):
    pointsArray = [int(inp) for inp in input().split(" ")]
    minPoint = min(pointsArray)
    l = len(pointsArray)

    cyclists = ["", ""]
    cyclistPoints = [list(), list()]
    for i in range(2):
        inp = input().split(" ")
        cyclists[i] = inp[0]
        for placement in inp[1:]:
            place = int(placement)
            if place <= l:
                cyclistPoints[i].append(pointsArray[place-1])

    S = sum(cyclistPoints[0]) - sum(cyclistPoints[1])
    divider = len(cyclistPoints[1]) - len(cyclistPoints[0])
    if S == 0:
        print(testNr + " ex aequo")
        if divider < 0:
            print(testNr + " " + cyclists[1] + " wint door verschuiving met -1")
            print(testNr + " " + cyclists[0] + " wint door verschuiving met 1")
        elif divider > 0:
            print(testNr + " " + cyclists[1] + " wint door verschuiving met 1")
            print(testNr + " " + cyclists[0] + " wint door verschuiving met -1")
    elif S > 0:
        print(testNr + " " + cyclists[0] + " wint")
        if divider < 0:
            S = math.fabs(S / divider)
            if S.is_integer() and minPoint - S > 0:
                S = int(S)
                print(testNr + f" ex aequo door verschuiving met {-S}")
            else:
                S = math.ceil(S)

            if minPoint - (S+1) > 0:
                print(testNr + " " + cyclists[1] + f" wint door verschuiving met {-(S+1)}")

        elif divider > 0:
            S = math.fabs(S / divider)
            if S.is_integer():
                S = int(S)
                print(testNr + " " + cyclists[1] + f" wint door verschuiving met {S + 1}")
                print(testNr + f" ex aequo door verschuiving met {S}")
            else:
                S = math.ceil(S)
                print(testNr + " " + cyclists[1] + f" wint door verschuiving met {S}")

    else:
        print(testNr + " " + cyclists[1] + " wint")
        if divider < 0:
            S = math.fabs(S / divider)
            if S.is_integer():
                S = int(S)
                print(testNr + " " + cyclists[0] + f" wint door verschuiving met {S + 1}")
                print(testNr + f" ex aequo door verschuiving met {S}")
            else:
                S = math.ceil(S)
                print(testNr + " " + cyclists[0] + f" wint door verschuiving met {S}")

        elif divider > 0:
            S = math.fabs(S / divider)
            if S.is_integer() and minPoint - S > 0:
                S = int(S)
                print(testNr + f" ex aequo door verschuiving met {-S}")
            else:
                S = math.ceil(S)
            if minPoint - (S+1) > 0:
                print(testNr + " " + cyclists[0] + f" wint door verschuiving met {-(S + 1)}")


if __name__ == '__main__':
    main()
