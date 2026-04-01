# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from collections import defaultdict
class Solution:
    def findCelebrity(self, n: int) -> int:
        
        graph = defaultdict(list)
        
        for curr in range(0, n):
            for person in range(0, n):
                if curr == person:
                    continue
                if knows(curr, person):
                    graph[curr].append(person)
                else:
                    graph[curr].append(-1)
        print(graph)
        res = -1
        for x in range(n):
            
            if max(graph[x]) == -1:
                temp = x
                for person in graph.keys():
                    if person == x:
                        continue
                    if x not in graph[person]:
                        temp = res
                res = temp
        
        return res