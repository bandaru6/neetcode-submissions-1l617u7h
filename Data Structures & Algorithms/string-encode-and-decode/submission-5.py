class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"
        string = ""
        for x in strs:
            string += x
            string += "-"
        return string[:-1]

    def decode(self, s: str) -> List[str]:
        
        return [] if s == "#" else s.split("-")
