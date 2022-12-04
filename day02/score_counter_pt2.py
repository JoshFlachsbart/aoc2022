""" Module to count RPS score with wins required """
win_score = { 'X':0, 'Y':3, 'Z':6 }
shape_score = { 'ROCK': 1 , 'PAPER': 2 ,  'SCIS': 3 }
outcomes = { 'A X' : 'SCIS',
    'A Y' : 'ROCK',
    'A Z' : 'PAPER',
    'B X' : 'ROCK',
    'B Y' : 'PAPER',
    'B Z' : 'SCIS',
    'C X' : 'PAPER',
    'C Y' : 'SCIS',
    'C Z' : 'ROCK' }

def calc_score():
    """ Calculate the total score from cheat sheet """
    elf_score = 0
    with open('data.txt', encoding='utf-8') as data_file:
        while data_file:
            line = data_file.readline().strip()
            if not line:
                break
            elf_score += win_score[line.split()[1]]
            elf_score += shape_score[outcomes[line]]
    return elf_score

print('Completed with 11657:', calc_score())
