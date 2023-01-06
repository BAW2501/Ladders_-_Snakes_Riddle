from itertools import product
r = list(range(101))  # rooms 1 to 100 ,  0is not used
r[4], r[5], r[19], r[28], r[35], r[44], r[53], r[59], r[70] = 75, 15, 41, 50, 96, 82, 94, 95, 91 # ladders
r[21], r[31], r[47], r[52], r[76], r[81], r[88], r[98] = 3, 8, 30, 23, 41, 62, 67, 12 # snakes


def move_player(pos, path, p_move, snake_or_ladder, room):
    pos += p_move
    if snake_or_ladder[pos]:
        snake_or_ladder[pos] = False
        pos = room[pos]
    path.append(pos)
    return pos, path


def play_game(player1_moves, player2_moves, room):
    pos1, pos2 = 1, 1  # player 1 and player 2 start at square 1
    snake_or_ladder = [i != v for i, v in enumerate(room)]
    path1, path2 = [1], [1]
    for p1_move, p2_move in zip(player1_moves, player2_moves):
        pos1, path1 = move_player(pos1, path1, p1_move, snake_or_ladder, room)
        pos2, path2 = move_player(pos2, path2, p2_move, snake_or_ladder, room)
    return pos1, path1, pos2, path2


# find path in 5 rolls meaning 4 rolls + 1 roll to get to 100 ,last roll is 100 - pos
for player1_moves in product(range(1, 7), repeat=4):
    for player2_moves in product(range(1, 7), repeat=4):
        p1_pos, path1, p2_pos, path2 = play_game(player1_moves, player2_moves, r)
        if p1_pos >= 94 and p2_pos >= 94:  # meaning one dice roll to get to 100
            print(player1_moves + (100 - p1_pos,), path2 + [100],player2_moves + (100 - p2_pos,), path1 + [100])

# (3, 1, 6, 5, 4) [1, 15, 41, 47, 94, 100]
# (4, 4, 6, 6, 6) [1, 75, 41, 30, 96, 100]
# (4, 4, 6, 5, 4) [1, 75, 41, 47, 94, 100]
# (3, 1, 6, 6, 6) [1, 15, 41, 30, 96, 100]