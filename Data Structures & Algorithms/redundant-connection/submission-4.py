class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)
        par = [i for i in range(N+1)]
        rank = [1] * (N + 1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
            else:
                par[p1] = p2
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        

        """
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

        """