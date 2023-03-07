import sys
from copy import deepcopy

inputFile = False


def runTest():
    streetPlan = inputTest()
    nodePlan = deepcopy(streetPlan)
    deadNodes = set()
    nodeFound = True
    while nodeFound:
        nodeFound = False
        for node, connections in list(nodePlan.items()):
            if len(connections) == 1:
                deadNodes.add(node)
                nodePlan.pop(node)
                nodePlan[connections[0]].remove(node)
                nodeFound = True
            elif len(connections) == 0:
                deadNodes.add(node)
                nodePlan.pop(node)
                nodeFound = True

    deadEnds = getDeadEnds(streetPlan, deadNodes)
    return deadEnds


def inputTest():
    numOfStreet = int(input())
    streetPlan = dict()
    for streets in range(numOfStreet):
        street = [int(node) for node in input().split()]
        if street[0] not in streetPlan:
            streetPlan[street[0]] = [street[1]]
        else:
            streetPlan[street[0]].append(street[1])
        if street[1] not in streetPlan:
            streetPlan[street[1]] = [street[0]]
        else:
            streetPlan[street[1]].append(street[0])
    return streetPlan


def getDeadEnds(streetPlan, deadNodes):
    deadEnds = set()
    liveNodes = set(streetPlan.keys()).difference(deadNodes)
    while len(liveNodes) != 0:
        undeadNodes = set()
        for node in liveNodes:
            for connection in streetPlan[node]:
                if connection in deadNodes:
                    deadEnds.add((node, connection))
                    deadNodes.remove(connection)
                    undeadNodes.add(connection)
        liveNodes = undeadNodes

    for node in deadNodes:
        for connection in streetPlan[node]:
            deadEnds.add((node, connection))

    return sorted(deadEnds)


def main():
    n = int(input())
    for test in range(n):
        deadEnds = runTest()
        print(test+1, end=" ")
        if len(deadEnds) == 0:
            print("geen")
            continue
        for i in range(len(deadEnds)):
            deadEnd = list(deadEnds)[i]
            if i != len(deadEnds) - 1:
                print(f"({deadEnd[0]},{deadEnd[1]}) ", end="")
            else:
                print(f"({deadEnd[0]},{deadEnd[1]})")


if __name__ == '__main__':
    if inputFile:
        with open("wedstrijd.invoer") as sys.stdin:
            main()
        sys.stdin = sys.__stdin__
    else:
        main()