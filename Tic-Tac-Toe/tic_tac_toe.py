grid = [[' '] * 3 for _ in range(3)]


def printer(grid):
    print("""---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------""".format(*[char for row in grid for char in row]))


def check(selection):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if selection[0] not in numbers or selection[1] not in numbers:
        print('You should enter numbers!')
        return True
    x, y = int(selection[0]), int(selection[1])
    if not 0 < x < 4 or not 0 < y < 4:
        print('Coordinates should be from 1 to 3!')
        return True
    if grid[3 - y][x - 1] != ' ':
        print('This cell is occupied! Choose another one!')
        return True


def win(grid):
    x_win, o_win = False, False
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2]:
            if grid[i][0] == 'X':
                x_win = True
            if grid[i][0] == 'O':
                o_win = True
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == 'X':
                x_win = True
            if grid[0][i] == 'O':
                o_win = True
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == 'X':
            x_win = True
        if grid[0][0] == 'O':
            o_win = True
    if grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[0][2] == 'X':
            x_win = True
        if grid[0][2] == 'O':
            o_win = True
    if x_win:
        return 'X wins'
    if o_win:
        return 'O wins'
    if ' ' not in [char for row in grid for char in row]:
        return 'Draw'


def main():
    is_x = True
    while True:
        printer(grid)
        while True:
            entry = input('Enter the coordinates: ').split()
            if check(entry):
                continue
            x, y = int(entry[0]), int(entry[1])
            if is_x:
                grid[3 - y][x - 1] = 'X'
                is_x = False
            else:
                grid[3 - y][x - 1] = 'O'
                is_x = True
            break
        if win(grid):
            printer(grid)
            print(win(grid))
            break


main()
