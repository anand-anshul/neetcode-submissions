class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visit = set()
        
        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)

        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs] == []:
                return True

            visit.add(crs)

            for nei in graph[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            return True

        for crs in graph.keys():
            if not dfs(crs):
                return False

        return True
