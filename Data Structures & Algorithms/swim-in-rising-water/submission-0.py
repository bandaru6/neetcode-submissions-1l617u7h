import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def dijkstra(start):
            dist = defaultdict(lambda: 10e9)
            dist[start] = grid[0][0]

            heap = [(grid[0][0], start)]

            neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while heap:
                cost, node = heapq.heappop(heap)

                if cost > dist[node]:
                    continue
                
                for neighbor in neighbors:
                    newx = node[0] + neighbor[0]
                    newy = node[1] + neighbor[1]

                    if newx < 0 or newx >= len(grid) or newy < 0 or newy >= len(grid[0]):
                        continue
                    newCost = max(grid[newx][newy], cost)
                    cell = (newx, newy)

                    if newCost < dist[cell]:
                        dist[cell] = newCost
                        heapq.heappush(heap, (newCost, cell))
            
            return dist[(len(grid) - 1, len(grid[0]) - 1)]
        
        return int(dijkstra((0,0)))


                
                