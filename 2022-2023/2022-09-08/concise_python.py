#!/usr/bin/env python

digit_binary = [f"{int(char):04b}" for char in input()]

for y in range(4):
	for x in range(4):
		char = "." if digit_binary[x][y] == "0" else "*"

		print(char, end="  " if x == 1 else " " if x < 3 else "")

	print()
