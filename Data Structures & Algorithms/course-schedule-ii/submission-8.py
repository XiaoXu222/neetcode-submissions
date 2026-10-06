class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

    


        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = set()
        visiting = set()
        courses = []
        
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
            courses.append(c)
            return True

        for cs in graph:
            if not dfs(cs, visiting):
                return []
       
        return courses
            
        