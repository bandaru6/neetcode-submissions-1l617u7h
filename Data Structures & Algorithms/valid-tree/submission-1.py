class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        
        return x

    def sameComponent(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        if self.sameComponent(x, y):
            return False
        
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        self.components -= 1

    def numComponents(self):
        return self.components


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf = UnionFind(n)

        for edge in edges:
            if uf.sameComponent(edge[0], edge[1]):
                return False
            uf.union(edge[0], edge[1])
        
        return uf.numComponents() == 1
        