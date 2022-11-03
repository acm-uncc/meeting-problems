#!/usr/bin/env python

import math

n = int(input())

triangle = []

for _ in range(n):
	row = list(map(int, input().split()))

	triangle.append(row)

cache_row = []

for i in range(n):
	new_row = []

	for j in range(i + 1):
		if i == 0:
			path_sum = triangle[i][j]
		elif j == 0:
			path_sum = cache_row[j] + triangle[i][j]
		elif j == i:
			path_sum = cache_row[j - 1] + triangle[i][j]
		else:
			path_sum = min(cache_row[j - 1], cache_row[j]) + triangle[i][j]

		new_row.append(path_sum)

	cache_row = new_row

temp = math.inf

for i in range(n):
	if cache_row[i] < temp:
		temp = cache_row[i]

print(temp)
