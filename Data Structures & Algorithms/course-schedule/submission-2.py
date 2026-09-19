class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[course].append(pre)

        visit = set()
        
        def dfs(i):
            if i in visit:
                return False
            if not graph[i]:
                return True
            
            visit.add(i)
            res = True
            for pre in graph[i]:
                res = res and dfs(pre)
            visit.remove(i)
            graph[i] = []
            return res
        
        for num in range(numCourses):
            if not dfs(num):
                return False
        
        return True
            
    

        
        