#!/usr/bin/env python

class Node:
	def __init__(self, value):
		self.value = value

		self.parent = None

n, m, q = map(int, input().split())

nodes = {}

for _ in range(n - 1):
	x, y = map(int, input().split())

	if x not in nodes:
		nodes[x] = Node(x)

	if y not in nodes:
		nodes[y] = Node(y)

	if nodes[x].parent is None:
		nodes[x].parent = y
	else:
		nodes[y].parent = x

for i in range(1, n + 1):
	nodes[i].digit = int(input())

for _ in range(q):
	a, b = map(int, input().split())

	a_ancestors = [a]
	b_ancestors = [b]

	b_ancestor_indices = {}

	while nodes[a_ancestors[-1]].parent is not None:
		a_ancestors.append(nodes[a_ancestors[-1]].parent)

	while nodes[b_ancestors[-1]].parent is not None:
		b_ancestors.append(nodes[b_ancestors[-1]].parent)

	for i, node in enumerate(b_ancestors):
		b_ancestor_indices[node] = i

	for i, node in enumerate(a_ancestors):
		if node in b_ancestor_indices:
			j = b_ancestor_indices[node]

			if j == 0:
				path = a_ancestors[:i + 1]
			else:
				path = a_ancestors[:i + 1] + b_ancestors[j - 1::-1]

			for i in range(len(path)):
				path[i] = nodes[path[i]].digit

			printable_path = "".join(map(str, path))

			print(int(printable_path) % m)

			break
