#!/usr/bin/env python

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

tree = TreeNode(2,
	TreeNode(1),
	TreeNode(3,
		TreeNode(0),
		TreeNode(1)
	)
)

def evaluateTree(root):
	if root.val == 0:
		return False
	
	if root.val == 1:
		return True

	if root.val == 2:
		return evaluateTree(root.left) or evaluateTree(root.right)

	return evaluateTree(root.left) and evaluateTree(root.right)

if evaluateTree(tree):
	print(1)
else:
	print(0)
