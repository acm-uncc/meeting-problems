#!/usr/bin/env python

def generate(num_rows):
	result = [[1]]

	for i in range(1, num_rows):
		result.append([1])

		for j in range(1, i):
			result[i].append(result[i - 1][j - 1] + result[i - 1][j])

		result[i].append(1)

	return result

print(generate(5))
