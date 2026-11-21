class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for val in range(n):
            adj[val] = []
        for u, v in edges:
            if u == v:
                return False
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n            
            
