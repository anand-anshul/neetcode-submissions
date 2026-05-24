class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        old2copy = {}
        visited = set()

        def dfs(node):
            if node in old2copy:
                return old2copy[node]

            node_cp = Node(node.val)
            old2copy[node] = node_cp

            for nei in node.neighbors:
                nei_cp = dfs(nei)
                node_cp.neighbors.append(nei_cp)

            return node_cp

        root_cp = dfs(node)
        return root_cp