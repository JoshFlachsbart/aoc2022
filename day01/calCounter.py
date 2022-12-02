def count():
	""" Count the number of items for each elf """
	elfCount = [0]
	elfNum = 0
	with open('data.txt') as dataFile:
		done = False
		while not done:
			line = dataFile.readline()
			if not line:
				done = True
				break
			if line.strip():
				elfCount[elfNum] += int(line)
			else:
				elfCount.append(0)
				elfNum += 1
	return elfCount
		
