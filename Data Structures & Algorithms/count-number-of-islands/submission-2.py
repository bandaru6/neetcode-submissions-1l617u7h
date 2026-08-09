class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0

        def bfs(loc):
            q = deque()
            q.append(loc)
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            while q:
                curr = q.pop()
                for direction in directions:
                    x = direction[0]
                    y = direction[1]
                    new = (curr[0] + x, curr[1] +y)
                    if new[0] >= 0 and new[0] < len(grid) and new[1] >= 0 and new[1] < len(grid[0]) and grid[new[0]][new[1]] == '1':
                        grid[new[0]][new[1]] = '0'
                        q.append(new)
            
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    bfs((x, y))
                    res += 1
        return res
        

        
