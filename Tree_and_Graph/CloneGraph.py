"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return
        copydic = {}
        self.buildDic(node, copydic)
        for Gnode in copydic:
            for neighbor in Gnode.neighbors:
                copydic[Gnode].neighbors.append(copydic[neighbor])
        return copydic[node]

        return node
    def buildDic(self, node, copydic):
        if node == None:
            return
        copiedNode = Node(val = node.val)
        copydic[node] = copiedNode
        for neighbor in node.neighbors:
            if neighbor not in copydic:
                self.buildDic(neighbor, copydic)