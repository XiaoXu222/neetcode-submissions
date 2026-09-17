"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        queue = collections.deque([node])
        # queue.append([node])
        oldToNew[node] = Node(node.val)

        while queue:
            for i in range(len(queue)):
                curNode = queue.popleft()
                
                for n in curNode.neighbors:
                    if n not in oldToNew:
                        oldToNew[n]= Node(n.val)
                        queue.append(n)
                    oldToNew[curNode].neighbors.append(oldToNew[n])

        return oldToNew[node]




        