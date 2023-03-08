def main():
    testCases = int(input())
    for test in range(testCases):
        runTest(test)


def runTest(testNr):
    width, height = [int(dimension) for dimension in input().split()]
    grid, boatPositions = inputGrid(width, height)
    grid = solveGrid(grid, boatPositions)

    N = 0
    for h in range(height):
        row = input()
        for w in range(width):
            box = row[w]
            if box in grid[(h, w)]:
                grid[(h, w)].remove(box)
            elif box not in {'.', '*'}:
                N += 1
    print(f"{testNr+1} {N}")


def solveGrid(grid, boatPositions):
    updated = True
    usedPos = set()
    while updated:
        updated = False
        newPos = set()
        for pos in boatPositions.difference(usedPos):
            for move in [(1, 0), (0, 1)]:
                r, c = map(sum, zip(pos, move))
                x, y = map(sum, zip(pos, [-m for m in move]))
                if withinBounds(r, c, grid):
                    if grid[(r, c)] == ['.']:
                        grid[(r, c)] = grid[pos]
                        newPos.add((r, c))
                        updated = True
                    elif grid[(r, c)] != ['*'] and withinBounds(x, y, grid):
                        if grid[(x, y)][0] not in {'.', '*'}:
                            grid[(r, c)].extend(grid[(x, y)])
                            grid[(x, y)] = grid[(r, c)]
                        else:
                            grid[(x, y)] = grid[pos]
                            newPos.add((x, y))
                        updated = True
            usedPos.add(pos)
        boatPositions.update(newPos)

    return grid


def inputGrid(width, height):
    grid = dict()
    boatPositions = set()
    for h in range(height):
        row = input()
        for w in range(width):
            box = row[w]
            grid[(h, w)] = [box]
            if box == '*':
                boatPositions.add((h, w))
    return grid, boatPositions


def withinBounds(x, y, grid):
    return (x, y) in grid


if __name__ == '__main__':
    main()
