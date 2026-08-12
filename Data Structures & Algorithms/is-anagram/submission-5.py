class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        dct = {}
        for i in s:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        for i in t:
            if i in dct:
                if dct[i] == 0:
                    return False
                dct[i] -= 1
            else:
                return False
        
        return True