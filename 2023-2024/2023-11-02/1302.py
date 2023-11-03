# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_depth(self, root):
        result = 0

        def dfs(node, depth):
            nonlocal result

            if node is None:
                if result < depth:
                    result = depth
            else:
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return result

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        root_max_depth = self.max_depth(root)
        result = 0

        def dfs(node, depth):
            nonlocal result

            if node is None:
                return

            if node.left is None and node.right is None:
                if depth == root_max_depth:
                    result += node.val
            else:
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root, 1)

        return result
