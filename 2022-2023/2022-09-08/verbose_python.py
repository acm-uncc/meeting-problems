#!/usr/bin/env python

digit_binary = []

for char in input():
	digit_binary.append(f"{int(char):04b}")

for y in range(4):
	for x in range(4):
		if digit_binary[x][y] == "0":
			char = "."
		else:
			char = "*"

		print(char, end="")

		if x == 1:
			print("  ", end="")
		elif x < 3:
			print(" ", end="")

	print()
