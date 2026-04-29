class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for pre, crs in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if crs not in preMap:
                preMap[crs] = set()
                for nei in graph[crs]:
                    preMap[crs] |= dfs(nei)
                preMap[crs].add(crs)
            return preMap[crs]    
        

        preMap = {} # crs : set

        for crs in range(numCourses):
            dfs(crs)

        res = []

        for u, v in queries:
            res.append(u in preMap[v])

        return res
