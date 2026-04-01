class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            length = min(len(w1), len(w2))
            if w1[:length] == w2[:length] and len(w2) < len(w1):
                return ""
            for c in range(length):
                if words[i][c] != words[i + 1][c]:
                    adj[words[i][c]].add(words[i + 1][c])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for char in adj[c]:
                if dfs(char):
                    return visit[c]
            visit[c] = False
            res.append(c)
        for c in adj.keys():
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)