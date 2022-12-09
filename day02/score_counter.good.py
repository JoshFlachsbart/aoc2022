""" Module to count RPS score with moves required """
shape_score = { 'ROCK':1, 'PAPER':2, 'SCIS':3 }
win_score = { 'WIN': 6 , 'LOSE': 0 ,  'DRAW': 3 }
codes = {
    'X' : ['ROCK', 'LOSE'],
    'Y' : ['PAPER', 'DRAW'],
    'Z' : ['SCIS', 'WIN']
}

outcomes = { 
    'A X' : ['DRAW', 'SCIS'],
    'A Y' : ['WIN', 'ROCK'],
    'A Z' : ['LOSE', 'PAPER'],
    'B X' : ['LOSE', 'ROCK'],
    'B Y' : ['DRAW', 'PAPER'],
    'B Z' : ['WIN', 'SCIS'],
    'C X' : ['WIN', 'PAPER'],
    'C Y' : ['LOSE', 'SCIS'],
    'C Z' : ['DRAW', 'ROCK'] 
}

def line_score_pt1(line):
    shape = codes[line.split()[1]][0]
    return shape_score[shape] + win_score[outcomes[line][0]]

def line_score_pt2(line):
    win = codes[line.split()[1]][1]
    return shape_score[outcomes[line][1]] + win_score[win]

def calc_score(score_func):
    """ Calculate the total score from cheat sheet """
    elf_score = 0
    with open('data.txt', encoding='utf-8') as data_file:
        while data_file:
            line = data_file.readline().strip()
            if not line:
                break
            elf_score += score_func(line)
    return elf_score

print('Completed pt 1 with 10816:', calc_score(line_score_pt1))
print('Completed pt 2 with 11657:', calc_score(line_score_pt2))