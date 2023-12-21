from copy import deepcopy
import moves as m


def position_cost (position):
    cost = m.calc_chekers(position, [1,3]) - m.calc_chekers(position, [2,4])
    return cost

# глубина = deep +2
# position = board, player = 'w''b', 
def minmax_algoritm(position, player, deep = 3):
    if   (player == 'w') & (m.calc_chekers(position, [1,3]) == 0): return -20
    elif (player == 'b') & (m.calc_chekers(position, [2,4]) == 0): return 20

    if deep == 0:
        return position_cost (position)
    # створюємо список всіх ходів
    list_moves = m.clear_moves(position, player)
    # якщо в нас немає ходів => нічия оцінка 0
    if list_moves == []:
        return 0
    # проходимо по цьому списку 
    cost_list = []
    for move in list_moves:
        # створюємо копію позиції
        new_position = deepcopy(position)
        # викониємо хід, отримаємо поле цього ходу
        m.do_move(new_position, move)
        # оцінку отримаємо 
        if player == 'w':
            cost_list += [minmax_algoritm(new_position, 'b', deep -1)]
        elif player == 'b':
            cost_list += [minmax_algoritm(new_position, 'w', deep -1)]

    if player == 'w':
        best_cost = max (cost_list)
    else :
        best_cost = min(cost_list)
    return best_cost


def root_minmax_algoritm (position, player, list_moves):
    
    cost_list = []
    for move in list_moves:
        # створюємо копію позиції
        new_position = deepcopy(position)
        # викониємо хід, отримаємо поле цього ходу
        m.do_move(new_position, move)
        # оцінку отримаємо 
        if player == 'w':
            cost_list += [minmax_algoritm(new_position, 'b')]
        elif player == 'b':
            cost_list += [minmax_algoritm(new_position, 'w')]
    
    if player == 'w':
        best_cost = max (cost_list)
    else :
        best_cost = min(cost_list)
    best_cost

    index = cost_list.index(best_cost)
    return list_moves[index]
