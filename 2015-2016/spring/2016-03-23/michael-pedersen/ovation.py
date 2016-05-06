#!/usr/bin/python3.5

#Author: Michael Pedersen

import sys

with open( sys.argv[1] ) as file_input:
	for lineCount, line in enumerate(file_input):
		audience = map(lambda x: int(x) if x.isdigit() else 0, list(line.split(" ")[1]))
		extraCount = 0
		currentCount = 0
		for shyness, numPeopleWithShyness in enumerate(audience):
			if (currentCount+extraCount) < shyness:
				extraCount+=1
			if numPeopleWithShyness != 0:
				currentCount += numPeopleWithShyness
		print("Case #" + str(lineCount+1) + ": " + str(extraCount))
