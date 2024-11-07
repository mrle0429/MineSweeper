# coding:utf-8
import random

def draw_dot(level):
    '''Mapping the upper boundary of the map'''
    print('  ', end='+')
    for i in range(level):
        print('---', end='+')
    print(" ")



def draw_head(level):
    '''Use numbers to represent vertical coordinates'''
    print('  ', end=' ')
    if level<10:
        for i in range(level):
            print(' '+str(i)+' ',end=' ')
    if level>10:
        for i in range(10):
            print(' '+str(i)+' ',end=' ')
        for j in range(10,level):
            print(' '+str(j)+'',end=' ')
    print()



def draw_board(board, level):
    '''print the grid'''
    print("Mines :", num_mines,"  Flags :",num_flag,"   No visible squares :",num_squares)
    draw_head(level)
    draw_dot(level)
    for i in range(level):
        print(chr(i+65)+" |",end="")
        for j in range(level):
            print(board[i][j],end="")
        print('\n  |' + '---+' * (level))



def new_board(level):
    '''print the axes'''
    board = []
    for x in range(level):
        board.append([])
        for y in range(level):
            board[x].append('   |')
    return board



def lay_mines(num_mines, level):
    '''set up mines randomly'''
    mines = []
    i = 0
    while i < num_mines:
        mine = [random.randint(0,level-1), random.randint(0,level-1)]
        if mine not in mines:
            mines.append(mine)
            i += 1
    return mines



def dig_mine(x, y, mines, level):
    '''find the mine by user'''

    if [x, y] in mines:
        board[x][y] = ' X |'

        return
    sum_mine = 0

    for xdirection, ydirection in CO:
        new_x = x
        new_y = y
        new_x =new_x+ xdirection
        new_y += ydirection
        if 0 <= new_x <level and 0 <= new_y < level:
            if [new_x, new_y] in mines:
                sum_mine += 1
    board[x][y] = " " + str(sum_mine) + ' |'

    if sum_mine == 0:
        board[x][y] = ' 0 |'
        for xdirection, ydirection in CO:
            new_x = x
            new_y = y
            new_x += xdirection
            new_y += ydirection
            if 0 <= new_x < level and 0 <= new_y < level:
                if board[new_x][new_y] != ' 0 |':
                    dig_mine(new_x, new_y, mines, level)



def setFlag(x,y):
    board[x][y]=' F |'



def is_win(board, mines, level):
    for i in range(level):
        for j in range(level):
            if [i, j] not in mines and board[i][j] == '   |':
                return False
    for i, j in mines:
        board[i][j] = ' X |'
    draw_board(board, level)


    print(f'Congratulations.')
    return True



def is_lose(board, mines, level):
    for i, j in mines:
        if board[i][j] == ' X |':
            for x, y in mines:
                board[x][y] = ' X |'
            draw_board(board, level)
            print('BOOM！You lost game T_T')
            return True
    return False


CO = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

while True:
    print('Welcome to Minesweeper .')

    #choose level and some key for user
    player_choose = input('''Please choose your difficulty :   
 1: Beginner 8 x 8 grid with 10 mines
 2: Intermediate 16 x 16 grid with 40 mines
 3: Expert 24 x 24 grid with 99 mines
 if you need help please input 'h' ''')
    if player_choose != '1' and player_choose != '2' and player_choose!='3':
        print('''Introduction about game:  For example 'A0'
            1.Select a grid and dig the mine : please input 'A0' or 'a0'
            2.Select a grid and place the flag: please input 'f a0' or 'F A0'
            ATTENTION!!! The F needs a space to separate it from the coordinates

            ''')
        continue
    if player_choose=='1':
        level=8
        num_mines=10
    if player_choose=='2':
        level=16
        num_mines=40
    if player_choose=='3':
        level=24
        num_mines=99
    num_flag=0
    num_squares=0

    board = new_board(level)
    for i in range(level):
        for j in range(level):
            num_squares += board[i][j].count('   |')
    mines = lay_mines(num_mines, level)
    draw_board(board, level)

    while True:
        num_squares=0
        move = input('Please enter your move :').upper()
        warning = 'Please inter correct, Such H3 or F H3:'
        if len(move) == 1:
            print(warning)

        if 2 <= len(move) <= 3:
            row = ord(move[0]) - 65
            column = int(move[1:])
            if board[row][column] != '   |':
                print("You've already opened this square, try another one")
            else:
                dig_mine(row, column, mines, level)

        if len(move) > 3:
            if move[0] == 'F':
                row = ord(move[2]) - 65
                column = int(move[3:])

                setFlag(row, column)
                num_flag+=1
        for i in range(level):
            for j in range(level):
                num_squares+=board[i][j].count('   |')



        if is_lose(board, mines, level) or is_win(board, mines, level):
            break
        draw_board(board, level)

    if not input('Continue playing?（y-Continue | n-Not continue）:').lower().startswith('y'):
        break
print('Game is over')