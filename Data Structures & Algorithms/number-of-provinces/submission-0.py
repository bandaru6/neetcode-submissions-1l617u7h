class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)) # [0, 1, 2, .. n]
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

        return True

    def numComponents(self):
        return self.components


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(len(isConnected))

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.numComponents()


        