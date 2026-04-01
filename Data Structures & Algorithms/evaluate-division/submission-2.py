class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        adj = defaultdict(list)

        for i in range(len(equations)):
            adj[equations[i][0]].append([equations[i][1], values[i]])
            adj[equations[i][1]].append([equations[i][0], 1/values[i]])

        res = []
        def bfs(query):
            src, target = query
            if src not in adj or target not in adj:
                return -1
            q = deque()
            visited = set()

            q.append([src, 1.0])
            visited.add(src)

            while q:
                node, val = q.popleft()
                if node == target:
                    return val
                for nei, weight in adj[node]:
                    if nei not in visited:
                        q.append([nei, val*weight])
                        visited.add(nei)
            
            return -1

        return [bfs(query) for query in queries]

