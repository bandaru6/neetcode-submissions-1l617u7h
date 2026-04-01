class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        if not grid:
            return 0

        def bfs(loc):
            r, c = loc
            q = deque()

            directions = [[1, 0],[-1, 0],[0, 1],[0, -1]]
            q.append([r, c])
            grid[r][c] = "0"

            while q:
                r, c = q.popleft()
                for direction in directions:
                    nr, nc = [direction[0] + r, direction[1] + c]
                    if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append([nr, nc])
        
        islands = 0

        for row in range(len(grid)):
            for c in range(len(grid[row])):
                if grid[row][c] == "1":
                    bfs([row, c])
                    islands += 1
        
        return islands