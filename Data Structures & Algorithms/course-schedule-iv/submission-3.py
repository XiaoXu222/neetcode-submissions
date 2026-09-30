class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {}
        for num in range(numCourses):
            graph[num] = []
        for pre, src in prerequisites:
            graph[src].append(pre)
        
        # visit = set()
        preMap = {}

        def dfs(i):
            if i in preMap:
                return preMap[i]
            # visit.add(i) 
            preMap[i] = set()         

            for p in graph[i]:
                preMap[i].add(p)
                for pre in dfs(p):
                    preMap[i].add(pre)
            
            return preMap[i]

        for i in range(numCourses):
            dfs(i)

        res = []
        for uj, vj in queries:
            if uj in preMap[vj]:
                res.append(True)
            else:
                res.append(False)
        return res





        