class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        distance = defaultdict(lambda: float("inf"))

        def bfs(loc):
            q = deque()
            q.append(loc)
            distance[loc] = 0

            directions = [(0,1),(1,0),(0,-1),(-1,0)]

            while q:
                curr = q.popleft()

                if grid[curr[0]][curr[1]] == 1 and distance[curr] > 0:
                    return distance[curr]

                for direction in directions:
                    cost = 0
                    newx = curr[0] + direction[0]
                    newy = curr[1] + direction[1]
                    if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]):
                        if grid[newx][newy] == 0:
                            cost = 1
                    else:
                        continue
                    
                    newDist = distance[curr] + cost

                    if newDist < distance[(newx, newy)]:
                        distance[(newx, newy)] = newDist

                        if cost == 0:
                            q.appendleft((newx, newy))
                        else:
                            q.append((newx, newy))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    return bfs((x, y))

                    

                    
                    

