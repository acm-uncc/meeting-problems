#!/usr/bin/env python

import itertools
import math

digits = [1, *map(int, input())]

occurences = [[0] * 9 for _ in range(9)]

for i in range(1, len(digits)):
	occurences[digits[i - 1] - 1][digits[i] - 1] += 1

result = math.inf

for permutation in itertools.permutations(list(range(9))):
	time = 0

	for i in range(9):
		for j in range(9):
			cost = abs(permutation[i] - permutation[j]) + 1

			time += cost * occurences[i][j]

	result = min(result, time - 1)

print(result)
