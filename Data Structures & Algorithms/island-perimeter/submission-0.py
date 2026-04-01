class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def bfs(x, y):
            q = deque()
            q.append([x,y])
            visited.add((x, y))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            res = 0
            while q:
                curr = q.pop()
                currSum = 4
                for direction in directions:
                    newx = direction[0] + curr[0]
                    newy = direction[1] + curr[1]

                    if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]):
                        if grid[newx][newy] == 1:
                            currSum -= 1
                            if (newx, newy) not in visited:
                                visited.add((newx, newy))
                                q.append([newx,newy])
                res += currSum
            return res


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return bfs(x, y)

        return 0

                