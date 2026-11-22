class dsu:
    def __init__(self, n):
        self.p = {label: label for label in range(n)}
        self.rank = {label: 0 for label in range(n)}
    
    def find(self, n):
        if n != self.p[n]:
            self.p[n] = self.find(self.p[n])
        return self.p[n]
    
    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.p[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.p[root1] = root2
        else:
            self.p[root2] = root1
            self.rank[root1] += 1

        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        DSU = dsu(n)
        for u, v in edges:
            if not DSU.union(u, v):
                return False
        root = DSU.find(0)
        for i in range(n):
            if DSU.find(i) != root:
                return False
        return True
            



        