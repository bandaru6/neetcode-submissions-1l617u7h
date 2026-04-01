class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for x in flights:
            graph[x[0]].append([x[1], x[2]])
        
        visited = set()
        def bfs(source, destination, cost, stops):

            q = deque()
            q.append([source, destination, 0, 0])
            cheapest = 10e9
            while q:
                curr = q.pop()
                if stops < curr[3]:
                    continue
                for x in graph[curr[0]]:
                    if x[0] == destination:
                        cheapest = min(cheapest, x[1] + curr[2])
                    else:
                        q.append([x[0], destination, curr[2] + x[1], curr[3] + 1])

            return cheapest if cheapest != 10e9 else -1
        
        return bfs(src, dst, 0, k)


