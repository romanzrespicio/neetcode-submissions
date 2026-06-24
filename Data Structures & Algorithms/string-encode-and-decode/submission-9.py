class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []

        for s in strs:
            out.append(str(len(s)) + '/' + s)

        return ''.join(out)

    def decode(self, s: str) -> List[str]:

        out = []
        i = 0
        j = i

        for i in range(len(s)):
            i = j
            if i == len(s):
                break
            while s[i] != '/':
                i += 1     
            length = int(s[j:i])
            i = i + 1
            j = i + length
            out.append(s[i:j])

        return out

