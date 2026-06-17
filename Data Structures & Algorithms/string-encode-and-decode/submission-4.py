class Solution:

    def encode(self, strs: List[str]) -> str:
        
        out = ""

        for s in strs:
            out += str(len(s)) + "#" + s
        
        return out
        

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = j + length + 1
            res.append(s[i:j])
            i = j

        return res
        
