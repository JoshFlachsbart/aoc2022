shapeScore = { 'X':1, 'Y':2, 'Z':3 }
winScore = { 'WIN': 6 , 'LOSE': 0 ,  'DRAW': 3 }
outcomes = { 'A X' : 'DRAW',
	'A Y' : 'WIN',
	'A Z' : 'LOSE',
	'B X' : 'LOSE',
	'B Y' : 'DRAW',
	'B Z' : 'WIN',
	'C X' : 'WIN',
	'C Y' : 'LOSE',
	'C Z' : 'DRAW' }

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
			elfScore += shapeScore[line.split()[1]]
			elfScore += winScore[outcomes[line]]
	return elfScore

