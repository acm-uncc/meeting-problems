"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def graphEdges(self, node):
        stack = [node]
        seen = set()
        result = {}

        while len(stack) > 0:
            node = stack.pop()

            if node in seen:
                continue
            
            seen.add(node)

            result[node.val] = []

            for neighbor in node.neighbors:
                result[node.val].append(neighbor.val)

            for neighbor in node.neighbors:
                stack.append(neighbor)

        return result

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        edges = self.graphEdges(node)
        nodes = {}

        for node in edges:
            nodes[node] = Node(node)
        
        for node in edges:
            for neighbor in edges[node]:
                nodes[node].neighbors.append(nodes[neighbor])
        
        return nodes[1]
