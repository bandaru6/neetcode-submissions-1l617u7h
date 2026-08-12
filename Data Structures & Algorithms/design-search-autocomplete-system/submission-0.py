class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.freq = 0
        self.sentence = ""

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):

        self.root = Node()
        for i in range(len(sentences)):
            sentence = sentences[i]
            curr = self.root
            for ch in sentence:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.end = True
            curr.freq += times[i]
            curr.sentence = sentence
        self.curr = self.root
        self.prefix = ""


    def input(self, c: str) -> List[str]:
        
        res = []
        if c == "#":
            curr = self.root
            for ch in self.prefix:
                if ch not in curr.children:
                    curr.children[ch] = Node()
                curr = curr.children[ch]
            curr.end = True
            curr.freq += 1
            curr.sentence = self.prefix

            self.curr = self.root
            self.prefix = ""
            return []


        self.prefix += c
        if c not in self.curr.children:
            self.curr.children[c] = Node()
        
        self.curr = self.curr.children[c]

        def dfs(node):
            if node.end:
                res.append((node.freq, node.sentence))
            
            for child in node.children:
                dfs(node.children[child])
        
        dfs(self.curr)

        res.sort(key = lambda x: (-x[0], x[1]))

        ans = []

        for freq, sentence in res[:3]:
            ans.append(sentence)

        return ans

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
