import bisect

word = input()
piece = input()
piece_set = set(piece)

pieces = set()

def dfs(rotated_piece, node):
	if len(node) == len(piece):
		return 1

	char = rotated_piece[len(node)]

	minimum_i = node[-1] + 1 if len(node) > 0 else 0

	num_solutions = 0

	if char not in char_indices:
		return 0

	i = bisect.bisect_left(char_indices[char], minimum_i)

	for j in char_indices[char][i:]:
		node.append(j)

		num_solutions += dfs(rotated_piece, node)

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
	result += dfs(rotated_piece, [])

print(result % 1000000007)
