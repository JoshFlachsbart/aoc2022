""" Module to count RPS score with moves required """
shape_score = { 'X':1, 'Y':2, 'Z':3 }
win_score = { 'WIN': 6 , 'LOSE': 0 ,  'DRAW': 3 }
outcomes = { 'A X' : 'DRAW',
    'A Y' : 'WIN',
    'A Z' : 'LOSE',
    'B X' : 'LOSE',
    'B Y' : 'DRAW',
    'B Z' : 'WIN',
    'C X' : 'WIN',
    'C Y' : 'LOSE',
    'C Z' : 'DRAW' }

def calc_score():
    """ Calculate the total score from cheat sheet """
    elf_score = 0
    with open('data.txt', encoding='utf-8') as data_file:
        while data_file:
            line = data_file.readline().strip()
            if not line:
                break
            elf_score += shape_score[line.split()[1]]
            elf_score += win_score[outcomes[line]]
    return elf_score

print('Completed with 10816:', calc_score())