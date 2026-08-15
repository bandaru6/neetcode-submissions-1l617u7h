class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}


        def dfs(i, j):

            if (i, j) in memo:
                return memo[(i, j)]
            
            if i >= len(word1):
                return len(word2) - j
            
            if j >= len(word2):
                return len(word1) - i


            if word1[i] == word2[j]:
                res = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1)) + 1
            
            memo[(i, j)] = res

            return memo[(i, j)]



        
        return dfs(0, 0)