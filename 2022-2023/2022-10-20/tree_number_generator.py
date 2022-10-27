#!/usr/bin/env python

class Node:
	def __init__(self, index):
		self.parent = None

		self.index = index

nodes = {}

n, m, q = map(int, input().split())

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

	while nodes[a_ancestors[-1]].parent is not None:
		a_ancestors.append(nodes[a_ancestors[-1]].parent)

	while nodes[b_ancestors[-1]].parent is not None:
		b_ancestors.append(nodes[b_ancestors[-1]].parent)

	b_ancestor_indices = {a: i for i, a in enumerate(b_ancestors)}

	for i, ancestor in enumerate(a_ancestors):
		if ancestor in b_ancestor_indices:
			j = b_ancestor_indices[ancestor]

			path = a_ancestors[1:i + 1] + b_ancestors[j - 1::-1]

			print("".join(str(nodes[node].digit) for node in path))

			break
