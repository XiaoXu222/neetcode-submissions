class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for num in range(numCourses):
            graph[num] = []
        for pre, src in prerequisites:
            graph[src].append(pre)
        
        visit = set()
        preMap = {}

        def dfs(i, visit):
            if i in visit:
                return preMap[i]
            visit.add(i) 
            preMap[i] = set()         

            for p in graph[i]:
                preMap[i].add(p)
                for pre in dfs(p, visit):
                    preMap[i].add(pre)
            
            return preMap[i]

        for i in range(numCourses):
            dfs(i, visit)

        res = []
        for uj, vj in queries:
            if uj in preMap[vj]:
                res.append(True)
            else:
                res.append(False)
        return res





        