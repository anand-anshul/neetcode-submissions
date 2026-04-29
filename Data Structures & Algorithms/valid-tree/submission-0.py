class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
       
        graph = {s : [] for s in range(n)}

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        visit = set()

        def dfs(src, prev):
            if src in visit:
                return False
            
            visit.add(src)
            for nei in graph[src]:
                if nei == prev:
                    continue
                if not dfs(nei, src):
                    return False
            return True
            

        return dfs(0, -1) and n == len(visit)
