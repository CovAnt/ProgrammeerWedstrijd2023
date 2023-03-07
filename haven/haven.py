def main():
    numTests = int(input())
    for test in range(numTests):
        runTest(test)


def runTest(testNr):
    w, h = [int(i) for i in input().split(" ")]

    grid, boatPositions = inputGrid(h, w)

    boatPositions = findAllBoatPositions(grid, boatPositions, set())
    updated = True
    while updated:
        updated = False
        for x, y in boatPositions:
            if (x+1 < len(grid) and x-1 >= 0) and \
                    (grid[x+1][y].difference(('.', '*')) != set() and grid[x-1][y].difference(('.', '*')) != set()):
                grid[x+1][y].update(grid[x-1][y])
                grid[x-1][y].update(grid[x+1][y])
                updated = True
            if (y+1 < len(grid[0]) and y-1 >= 0) and \
                    (grid[x][y+1].difference(('.', '*')) != set() and grid[x][y-1].difference(('.', '*')) != set()):
                grid[x][y+1].update(grid[x-1][y])
                grid[x][y-1].update(grid[x+1][y])
                updated = True
            boatPositions.remove((x, y))

    grid2, boatPositions = inputGrid(h, w)
    N = 0
    for x in range(h):
        for y in range(w):
            if grid2[x][y].difference(grid[x][y]) != set():
                N += 1
    print(f"{testNr+1} {N}")


def inputGrid(h, w):
    grid = [[set() for width in range(w)] for height in range(h)]
    boatPositions = set()
    for height in range(h):
        row = input()
        for width in range(w):
            compartment = row[width]
            if compartment == '*':
                grid[height][width].add('.')
                boatPositions.add((height, width))
            grid[height][width].add(compartment)
    return grid, boatPositions


def findAllBoatPositions(grid, boatPositions, usedPositions):
    while len(boatPositions.difference(usedPositions)) != 0:
        for x, y in boatPositions.difference(usedPositions):
            if x + 1 < len(grid) and grid[x + 1][y] == '.':
                grid[x + 1][y].add('*')
                boatPositions.add((x + 1, y))
            if x - 1 >= 0 and grid[x - 1][y] == '.':
                grid[x - 1][y].add('*')
                boatPositions.add((x + 1, y))
            if y + 1 < len(grid[0]) and grid[x][y + 1] == '.':
                grid[x][y + 1].add('*')
                boatPositions.add((x + 1, y))
            if y - 1 >= 0 and grid[x][y - 1] == '.':
                grid[x][y - 1].add('*')
                boatPositions.add((x + 1, y))
            usedPositions.add((x, y))

    return boatPositions


if __name__ == '__main__':
    main()
