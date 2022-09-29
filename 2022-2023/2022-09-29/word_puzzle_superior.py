word = input()
piece = input()

rotated_pieces = set()

for i in range(0, len(piece)):
	rotated_pieces.add(piece[i:] + piece[:i])

result = 0

for rotated_piece in rotated_pieces:
	dp_row = [1] + [0] * len(piece)

	for y in range(1, len(word) + 1):
		for x in range(len(piece), 0, -1):
			combos = dp_row[x]

			if rotated_piece[x - 1] == word[y - 1]:
				combos += dp_row[x - 1]

			dp_row[x] = combos

	result += dp_row[len(piece)]

print(result % 1000000007)
