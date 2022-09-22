word = input()
piece = input()
piece_set = set(piece)

pieces = set()

def dfs(node):
	if len(node) == len(piece):
		return 1

	char = piece[len(node)]

	minimum_i = node[-1] + 1

	num_solutions = 0

	for i in char_indices[char]:
		if i >= minimum_i:
			node.append((char, i))

			num_solutions += dfs(node)

			node.pop()

	return num_solutions

for i in range(len(piece)):
	pieces.add(piece[i:] + piece[:i])

char_indices = {}

for i, char in enumerate(word):
	if char in piece_set:
		if char not in char_indices:
			char_indices[char] = []

		char_indices[char].append(i)

result = 0

for rotated_piece in pieces:
	result += dfs([])
