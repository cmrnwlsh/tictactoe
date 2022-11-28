grid = [['.'] * 3 for i in range(0, 3)]
finished = False
turn = True

while not finished:
    for row in grid:
        print(row)
    print('player 1' if turn else 'player 2', end=' ')
    target = input('enter coordinates: ').split()

    if len(target) != 2 or any(not item.isdigit() or
                               int(item) > 2 or int(item) < 0
                               for item in target):
        continue

    symbol = 'x' if turn else 'o'

    if grid[int(target[0])][int(target[1])] != '.':
        continue

    grid[int(target[0])][int(target[1])] = symbol
    if any([all(item == symbol for item in grid[0]),
            all(item == symbol for item in grid[1]),
            all(item == symbol for item in grid[2]),
            all(item == symbol for item in [grid[0][0], grid[1][0], grid[2][0]]),
            all(item == symbol for item in [grid[0][1], grid[1][1], grid[2][1]]),
            all(item == symbol for item in [grid[0][2], grid[1][2], grid[2][2]]),
            all(item == symbol for item in [grid[0][0], grid[1][1], grid[2][2]]),
            all(item == symbol for item in [grid[2][0], grid[1][1], grid[0][2]])]):
        for row in grid:
            print(row)
        print(('player 1' if turn else 'player 2') + ' wins')
        finished = True

    turn = not turn
