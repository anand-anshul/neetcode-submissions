class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        graph = defaultdict(list)

        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for nei in graph[i]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res