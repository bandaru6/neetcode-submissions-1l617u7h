class UnionFind:
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n 
        self.components = n
        
    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        root_x = self.find(x)
        root_y = self.find(y)

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        self.components -= 1
        return True


        
        

    def getNumComponents(self) -> int:
        return self.components


