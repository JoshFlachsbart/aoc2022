""" Module to find visible trees """

Dir = {
    'UP' : 0,
    'RIGHT': 1,
    'DOWN': 2,
    'LEFT': 3
}

class Tree:
    """ Wow was this overkill. Was so sure I was going to need more structure when we hit part 2. """
    height: int
    viz: list
    view: list

    def __init__(self, height):
        self.height = height
        self.viz = [False, False, False, False]
        self.view = [0,0,0,0]
    
    def __repr__(self):
        return f"[{self.height}:{self.is_viz()}:{self.cal_view()}]"
 
    def is_viz(self):
        return True in self.viz
    
    def mark_viz(self, from_direction):
        self.viz[from_direction] = True

    def mark_view(self, dir, val):
        self.view[dir] = val

    def cal_view(self):
        prod = 1
        for view in self.view:
            prod *= view
        return prod

def update_row_viz_dir(forest_row, dir):
    highest = -1
    for tree in forest_row:
        if tree.height > highest:
            tree.viz[dir] = True
            highest = tree.height

def update_row_view_dir(this_tree, forest_row, dir):
#    print(this_tree, forest_row)
    for tree in forest_row:
        this_tree.view[dir] += 1
        if tree.height >= this_tree.height:
            break

def update_viz(forest):
    for col_num in range(len(forest[0])):
        forest_col = [tree_row[col_num] for tree_row in forest]
        update_row_viz_dir(forest_col, Dir['UP'])
        update_row_viz_dir(reversed(forest_col), Dir['DOWN'])

    for forest_row in forest:
        update_row_viz_dir(forest_row, Dir['LEFT'])
        update_row_viz_dir(reversed(forest_row), Dir['RIGHT'])
#        print(forest_row)

def update_view(forest):
    for col_num in range(len(forest[0])):
        forest_col = [tree_row[col_num] for tree_row in forest]
        for i in range(len(forest_col)):
            update_row_view_dir(forest_col[i],reversed(forest_col[:i]), Dir['UP'])
            update_row_view_dir(forest_col[i], forest_col[i+1:], Dir['DOWN'])

    for forest_row in forest:
        for i in range(len(forest_row)):
            update_row_view_dir(forest_row[i],reversed(forest_row[:i]), Dir['LEFT'])
            update_row_view_dir(forest_row[i], forest_row[i+1:], Dir['RIGHT'])
#        print(forest_row)

def load_forest(file_name):
    """ Read text forest description into array """
    all_lines = []
    with open(file_name, encoding='utf-8') as data_file:
        all_lines = [line.strip() for line in data_file]

    forest = []
    for line in all_lines:
        forest_row = []
        for height in line:
            forest_row.append(Tree(int(height)))
        forest.append(forest_row)

    return forest

def run():
    forest = load_forest('data.txt')
    update_viz(forest)
    update_view(forest)

    max = 0
    count = 0
    for row in forest:
        for tree in row:
            if tree.is_viz():
                count += 1
            if tree.cal_view() > max:
                max = tree.cal_view()


    print('Part 1 1849:', count) 
    print('Part 2 201600:', max) 


run()
