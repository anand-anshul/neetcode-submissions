class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c : [] for c in range(numCourses)}
        for src, dst in prerequisites:
            graph[src].append(dst)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output


            