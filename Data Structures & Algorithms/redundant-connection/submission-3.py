class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        dupes = []
        for edge in edges:
            if edge[0] in visited and edge[1] in visited:
                dupes.append(edge)
            visited.add(edge[0])
            visited.add(edge[1])

        def bfs(edge):
            start = edge[0]
            end = edge[1]
            q = deque()
            res = False

            seen = {start}
            q.append(start)
            graph[start].remove(end)
            graph[end].remove(start)
            while q:
                curr = q.pop()
                if curr == end:
                    res = True
                    break
                for e in graph[curr]:
                    if e not in seen:
                        q.append(e)
                        seen.add(e)
            graph[start].append(end)
            graph[end].append(start)
            return res
        for x in range(len(dupes), -1, -1):
            if bfs(dupes[x - 1]):
                break
            dupes.pop()

        return dupes[-1]