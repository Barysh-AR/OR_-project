import algoritm 
import moves as m

board = [
         [0,2,0,2,0,2,0,2],
         [2,0,2,0,2,0,2,0],
         [0,2,0,2,0,2,0,2],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,0,1,0,1,0,1,0],
         [0,1,0,1,0,1,0,1],
         [1,0,1,0,1,0,1,0]
         ]


def human_choise(moves):
    # виводимло можливі ходи
    print ("Ваш хід")
    n = 0
    for i in moves:
        print(str(n) + ") " + str(i))
        n += 1
    # очікуємо вибір ходу
    choice = int(input())
    
    return moves[choice]


def pleer_go (board, color):
    game_over = False
    # створюємо список допустимих ходів
    moves = m.clear_moves (board, color)
    
    if moves != []: 
        # обираємо хід
        if color in human_chekers:
            choice = human_choise(moves)
        else: 
            # choice = bot_choise(board, color, moves)
            choice = algoritm.root_minmax_algoritm (board, color, moves)
        # робимо хід
        m.do_move(board, choice)
        # перевіряємо чи залишились в супротивника шашки
        if   (color == 'w') & (m.calc_chekers(board, [2,4]) == 0): game_over = True
        elif (color == 'b') & (m.calc_chekers(board, [1,3]) == 0): game_over = True
    else :
        game_over = True
    return game_over


game_end = False
current_player = 'w'

# human_chekers = [] # грає тільки бот
human_chekers = ['w'] # людина грає за білих
# human_chekers = ['b'] # людина грає за чорних
# human_chekers = ['w','b'] #людина грає за всіх

moves_after_the_beating = 0
now_old_chekers = 24 
while not(game_end):
    m.print_board (board)

    if current_player == 'w':
        print("Хід білих")
        game_end = pleer_go (board, 'w')
        current_player = 'b'
    elif current_player == 'b':
        print("Хід чорних")
        game_end = pleer_go (board, 'b')
        current_player = 'w'
    
    now_chekers = m.calc_chekers(board, [1,3,2,4])
    if now_old_chekers != now_chekers:
        moves_after_the_beating = 0
        now_old_chekers = now_chekers
    else:
        moves_after_the_beating += 1
    
    if moves_after_the_beating == 24:
        game_end = True
        print("Гра закінчилася нічиєю")
    

m.print_board (board)