class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        def bfs(i, j):
            q = deque()
            local_area = 0
            q.append([i,j])
            grid[i][j] = 0
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            while q:
                curr = q.pop()
                local_area += 1
                for direction in directions:
                    i, j = (curr[0] + direction[0], curr[1] + direction[1])
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                        if grid[i][j] == 1:
                            q.append([i, j])
                            grid[i][j] = 0
            return local_area

        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    area = max(area, bfs(i, j))
        
        return area
