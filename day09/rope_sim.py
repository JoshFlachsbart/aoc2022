""" Module to simulate rope movement """

visited_hash = {}
visited_hash_2 = {}
head_loc = [0,0]
tail_loc = [0,0]
knots = [[0,0] for i in range(10)]

def move_tail(head_loc, tail_loc):
    new_loc = [tail_loc[0], tail_loc[1]]
    x_dist = head_loc[0] - tail_loc[0]
    y_dist = head_loc[1] - tail_loc[1]
    if abs(x_dist) <= 1 and abs(y_dist) <= 1:
        new_loc = tail_loc
    else:
        if y_dist != 0:
            if (y_dist > 0):
                new_loc[1] += 1
            elif (y_dist < 0):
                new_loc[1] -= 1
        if x_dist != 0:
            if (x_dist > 0):
                new_loc[0] += 1
            elif (x_dist < 0):
                new_loc[0] -= 1
    return new_loc

def move_tail_2(head_loc, tail_loc):
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

def move_head_2(command):
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
            move_tail_2(prev, knot)
            prev = knot
        
        tail_loc = knots[-1]
        loc_string = f'{tail_loc[0]},{tail_loc[1]}'
#        print(loc_string)
        if loc_string not in visited_hash:
            visited_hash_2[loc_string] = True

def move_head(command):
    (dir, dist) = command.split()
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

        move_tail_2(head_loc, tail_loc)
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
    for move in load_moves('data.txt'):
#        move_head(move)
        move_head_2(move)

#    print ('Part 1 6337:', len(visited_hash))
    print ('Part 2 36:', len(visited_hash_2))

run()