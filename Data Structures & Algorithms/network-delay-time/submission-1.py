import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for ui, vi, ti in times:
            adj[ui].append([vi, ti])

        mintimes = [float("inf")] * (n + 1)
        mintimes[0] = 0

        heap = []

        # time, src, target
        heapq.heappush(heap, [0, k, k])

        while heap:
            time, src, target  = heapq.heappop(heap)

            mintimes[target] = min(mintimes[target], time)

            for node, t in adj[target]:
                newTime = t + time
                
                if newTime < mintimes[node]:
                    mintimes[node] = min(mintimes[node], newTime)
                    heapq.heappush(heap, [newTime, target, node])
        
        return -1 if max(mintimes) == float("inf") else int(max(mintimes))



