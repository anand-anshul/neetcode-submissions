class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return
            
            visit.add(crs)

            for nei in graph[crs]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1

        return res