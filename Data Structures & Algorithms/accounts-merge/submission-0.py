class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        emailGraph = defaultdict(list)
        emailToName = {}
        

        for account in accounts:
            name = account[0]
            first = account[1]
            for idx in range(1, len(account)):
                email = account[idx]
                emailToName[email] = name
                emailGraph[first].append(email)
                emailGraph[email].append(first)
        
        visited = set()
        res = []
        def dfs(email):
            visited.add(email)
            currEmails = [email]

            for nei in emailGraph[email]:
                if nei not in visited:
                    currEmails += dfs(nei)
            return currEmails
        
        for email in emailGraph.keys():
            if email not in visited:
                emails = dfs(email)
                emails.sort()
                res.append([emailToName[email]] + emails)

        return res
        

            
