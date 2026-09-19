class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visit = set()
        path = set()
        res = []

        def dfs(crs):
            if crs in visit:
                return False
            if crs in path:
                return True
            
            visit.add(crs)
            if graph[crs]:
                for pre in graph[crs]:
                    if not dfs(pre):
                        return False
            visit.remove(crs)
            path.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
        