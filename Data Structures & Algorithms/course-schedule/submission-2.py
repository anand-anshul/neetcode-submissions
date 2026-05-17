class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        visited = set()

        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)

        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True

            visited.add(crs)

            for pres in graph[crs]:
                if not dfs(pres):
                    return False
            visited.remove(crs)

            return True

        for crs in graph.keys():
            if not dfs(crs):
                return False

        return True
                
