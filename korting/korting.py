import math


def main():
    numOfTests = int(input())
    for test in range(numOfTests):
        runTest(test)


def runTest(testNr):
    numOfCustomers = int(input())
    discountNomDenoms = [[0, 1] for customer in range(numOfCustomers)]
    customers = set()
    day = [int(customer) for customer in input().split(" ")]
    for customer in day:
        if customer in customers:
            customers.remove(customer)
        else:
            fN = 2**(len(customers))
            for client in customers:
                nom, denom = discountNomDenoms[client - 1]
                nom = nom*fN + denom
                denom *= fN
                discountNomDenoms[client - 1] = [nom, denom]
            customers.add(customer)

    for customer in range(numOfCustomers):
        nom, denom = discountNomDenoms[customer]
        GCD = math.gcd(nom, denom)
        nom //= GCD
        denom //= GCD
        if nom/denom > 0.73:
            nom = 73
            denom = 100

        if nom != 0:
            print(f"{testNr+1} {customer+1} {nom}/{denom}")
        else:
            print(f"{testNr+1} {customer+1} 0")


if __name__ == '__main__':
    main()
