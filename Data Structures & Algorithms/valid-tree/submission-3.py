class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        treeMap = {}
        for val in range(n):
            treeMap[val] = set()
        for edge in edges:
            if edge[0] == edge[1]:
                return False
            treeMap[edge[0]].add(edge[1])
            treeMap[edge[1]].add(edge[0])

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for nei in treeMap[node]:
                if nei == parent:
                    continue

                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n            
            
