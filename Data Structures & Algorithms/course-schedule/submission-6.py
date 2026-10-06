class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        visiting = set()
        
        def dfs(c, visiting):
            if c in visiting:
                return False
            if c in visited:
                return True

            visiting.add(c)

            for p in graph[c]:
                if not dfs(p, visiting):
                    return False
            visited.add(c)        
            visiting.remove(c)
            return True

        for cs in graph:
            if not dfs(cs, visiting):
                return False
       
        return True
            
        

        
        