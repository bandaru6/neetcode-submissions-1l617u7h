class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        res = []
        visited = set()

        def dfs(start, goal, cost):
            if start in transitions:
                for transition in transitions[start]:
                    found = -1
                    if transition[0] == goal:
                        return cost*transition[1]
                    if transition[0] not in visited:
                        visited.add(transition[0])
                        found = dfs(transition[0], goal, cost*transition[1])
                    if found != -1:
                        return found
            return -1

        

        transitions = defaultdict(list)
        for index, value in enumerate(equations):
            transitions[value[0]].append([value[1], values[index]])
            transitions[value[1]].append([value[0], 1/values[index]])

        for query in queries:
            res.append(dfs(query[0], query[1], 1))
            visited = set()
            

        return res
        
