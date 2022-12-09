""" Module to simulate rope movement """

def move_tail(head_loc, tail_loc):
    x_dist = head_loc[0] - tail_loc[0]
    y_dist = head_loc[1] - tail_loc[1]
    if not (abs(x_dist) <= 1 and abs(y_dist) <= 1):
        if y_dist != 0:
            if (y_dist > 0):
                tail_loc[1] += 1
            elif (y_dist < 0):
                tail_loc[1] -= 1
        if x_dist != 0:
            if (x_dist > 0):
                tail_loc[0] += 1
            elif (x_dist < 0):
                tail_loc[0] -= 1

def test_tail():
    print('[1,1]:', move_tail([0,0],[1,1]))
    print('[4,2]:', move_tail([4,2],[4,2]))
    print('[4,2]:', move_tail([4,1],[4,3]))
    print('[4,2]:', move_tail([4,3],[4,1]))
    print('[4,1]:', move_tail([5,1],[3,1]))
    print('[4,2]:', move_tail([3,2],[5,2]))
    print('[2,1]:', move_tail([3,2],[2,1]))
    print('[3,2]:', move_tail([3,3],[2,1]))

#test_tail()

def move_head(command, knots, visited_hash):
    (dir, dist) = command.split()
    head_loc = knots[0]
    # I WANNA USE MATCH.  Upgrate to python 3.10 or newer?
    for i in range(int(dist)):
        if dir == 'U':
            head_loc[1] += 1
        elif dir == 'D':
            head_loc[1] -= 1
        elif dir == 'R':
            head_loc[0] += 1
        elif dir == 'L':
            head_loc[0] -= 1
        
        prev = head_loc
        for knot in knots[1:]: 
            move_tail(prev, knot)
            prev = knot
        
        tail_loc = knots[-1]
        loc_string = f'{tail_loc[0]},{tail_loc[1]}'
#        print(loc_string)
        if loc_string not in visited_hash:
            visited_hash[loc_string] = True

def load_moves(file_name):
    """ Read the rope moves into array """
    all_lines = []
    with open(file_name, encoding='utf-8') as data_file:
        all_lines = [line.strip() for line in data_file]
    
    return all_lines

def run():
    visited_hash_1 = {}
    visited_hash_2 = {}
    knots_1 = [[0,0] for i in range(2)]
    knots_2 = [[0,0] for i in range(10)]

    for move in load_moves('data.txt'):
        move_head(move, knots_1, visited_hash_1)
        move_head(move, knots_2, visited_hash_2)

    print ('Part 1 6337:', len(visited_hash_1))
    print ('Part 2 2455:', len(visited_hash_2))

run()