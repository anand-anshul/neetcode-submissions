class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int: 
        uf = UnionFind(n)
        res = n
        for v1, v2 in edges:
            res -= uf.union(v1, v2)
        return res



class UnionFind:
    def __init__(self, size) -> None:
        self.parents = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if x == self.parents[x]:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rep_x, rep_y = self.find(x), self.find(y)
        if rep_x == rep_y:
            return 0
        if True:
            if self.size[rep_x] >= self.size[rep_y]:
                self.parents[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]

            else:
                self.parents[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
        return 1

    def get_size(self, x):
        return self.size[self.find(x)]