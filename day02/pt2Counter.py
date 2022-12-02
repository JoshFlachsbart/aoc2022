winScore = { 'X':0, 'Y':3, 'Z':6 }
shapeScore = { 'ROCK': 1 , 'PAPER': 2 ,  'SCIS': 3 }
outcomes = { 'A X' : 'SCIS',
	'A Y' : 'ROCK',
	'A Z' : 'PAPER',
	'B X' : 'ROCK',
	'B Y' : 'PAPER',
	'B Z' : 'SCIS',
	'C X' : 'PAPER',
	'C Y' : 'SCIS',
	'C Z' : 'ROCK' }

def calcScore():
	""" Calculate the total score from cheat sheet """
	elfScore = 0
	with open('data.txt') as dataFile:
		done = False
		while not done:
			line = dataFile.readline().strip()
			if not line:
				done = True
				break
			elfScore += winScore[line.split()[1]]
			elfScore += shapeScore[outcomes[line]]
	return elfScore

