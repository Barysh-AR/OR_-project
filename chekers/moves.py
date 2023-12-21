# 0 - порожня клітина
# 1 - біла шашка
# 2 - чорна шашка
# 3 - біла дамка
# 4 - чорна дамка

# дошка, список тих шашок що рахуємо [1,2,3,4]
def calc_chekers (board, list1):
    n = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] in list1: n+=1
    return n

def print_board (board):
    print("* 0 1 2 3 4 5 6 7 ")
    row_num = 0
    for row in board:
        print(str(row_num)+"|", end='')
        for el in row:
            if el == 0:
                print (" |", end='')
            elif el == 1:
                print ("o|", end='')
            elif el == 2:
                print ("b|", end='')
            elif el == 3:
                print ("Q|", end='')
            elif el == 4:
                print ("B|", end='')
        row_num+=1
        print()

# координата [x,y]
# хід [КООРДИНАТА старого положення, КООРДИНАТА нового положення, СПИСОК координат шашок що будуть побиті]
# хід [СПИСОК int, СПИСОК int, СПИСОК СПИСКІВ int]

# видалення шашки з поля
def delite_checker(board, coord):
    board [coord[0]][coord[1]] = 0
def delite_checkers(board, coords):
    for coord in coords:
        delite_checker(board, coord)
# створення шашки на полі
def create_checker(board, coord, tipe):
    board [coord[0]][coord[1]] = tipe

# виконати хід на дошці
def do_move (board, move):
    if move == []: pass
    # move = old position, new position, list hitting checkers

    # create position = new position
    tipe_cheker = board [move[0][0]][move[0][1]]
    if (tipe_cheker == 1) & (move[1][0] == 0):
        create_checker(board, move[1], 3)
    elif (tipe_cheker == 2) & (move[1][0] == 7):
        create_checker(board, move[1], 4)
    else : 
        create_checker(board, move[1], tipe_cheker)
    # delite position = [old position] + hitting checkers
    delite_checkers(board, [move[0]] + move[2])


def filt(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

# перевірити чи координата знаходиться на дошці
def coord_in_board(coord):
    # x,y in [0,7] 
    return (0 <= coord[0] <= 7) & (0 <= coord[1] <= 7)
# перевірити чи шашки за двома координатами одного кольору
def same_color(checker1, checker2):
    if   (checker1 in (1,3)) & (checker2 in(1,3)): return True
    elif (checker1 in (2,4)) & (checker2 in(2,4)): return True
    else : return False
# отримати список ходів атаки для певного початкового положення
def give_atak_moves (board, current, tipe, moves, start):

    def give_attacked_from_move(move):
        return move[2]
    def give_attacked_from_moves(moves):
        result = []
        for move in moves:
            result += give_attacked_from_move(move)
        return result

    already_attacked = give_attacked_from_moves(moves)

    def check_direction(current, x, y):
        attacked = [current[0] + x,current[1] + y]
        new = [current[0] + 2*x,current[1] + 2*y]

        if not( coord_in_board(attacked) & coord_in_board(new) ):
            return []
        elif   same_color (board [attacked[0]][attacked[1]], tipe): 
            return []
        elif board [new[0]][new[1]] != 0 :
            return []
        elif board [attacked[0]][attacked[1]] == 0:
            return []
        elif attacked in already_attacked:
            return []
        else: 
            this_move = [start,new,already_attacked + [attacked]]
            return give_atak_moves (board, new, tipe, moves + [this_move], start)

    result = moves[:]

    if   tipe == 1:
        result += check_direction(current, -1, 1)
        result += check_direction(current, -1, -1)
    elif tipe == 2:
        result += check_direction(current, 1, 1)
        result += check_direction(current, 1, -1)
    elif tipe in (3,4):
        result += check_direction(current, -1, 1)
        result += check_direction(current, -1, -1)
        result += check_direction(current, 1, 1)
        result += check_direction(current, 1, -1)
    
    return filt(result)
# отримати ходи які може зробити шашка за координатою
def give_moves_this_cheker(board, coord):
    
    tipe_this = board [coord[0]][coord[1]]
    moves = []

    def sortPosition(p):
        result = []
        if not(coord_in_board(p)):
            return []
        elif board [p[0]][p[1]] != 0:
            return []
        else: result += [[coord, p, []]]
        return result

    if   tipe_this == 1:
        moves += sortPosition([coord[0]-1,coord[1]+1])
        moves += sortPosition([coord[0]-1,coord[1]-1])
    elif tipe_this == 2:
        moves += sortPosition([coord[0]+1,coord[1]+1])
        moves += sortPosition([coord[0]+1,coord[1]-1])
    elif tipe_this in (3,4):
        moves += sortPosition([coord[0]-1,coord[1]+1])
        moves += sortPosition([coord[0]-1,coord[1]-1])
        moves += sortPosition([coord[0]+1,coord[1]+1])
        moves += sortPosition([coord[0]+1,coord[1]-1])
    
    moves += give_atak_moves(board, coord, board[coord[0]][coord[1]], [], coord)
    return moves

# отримати всі ходи, які можливо зробити для одного кольору
def give_moves_all_cheker(board, color):
    all_moves = []
    if   color == 'w':
        for i in range(8):
            for j in range(8):
                if board [i][j] in (1,3):
                    all_moves += give_moves_this_cheker(board, [i,j])
    elif color == 'b':
        for i in range(8):
            for j in range(8):
                if board [i][j] in (2,4):
                    all_moves += give_moves_this_cheker(board, [i,j])
    return all_moves

# генерує ві можливі ходи, і якщо є ходи атаки, то залишає тільки їх
def clear_moves(board, color):
    ataked = False
    clear_moves = []

    moves = give_moves_all_cheker(board, color)
    for move in moves:
        if move[2] != []: ataked = True

    if ataked:
        for move in moves:
            if move[2] != []: clear_moves += [move]
        return clear_moves
    else :
        return moves

