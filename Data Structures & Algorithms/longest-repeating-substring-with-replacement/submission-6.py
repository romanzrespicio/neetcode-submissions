class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = {}
        L = 0
        maxF = 0
        maxLen = 0

        for R in range(len(s)):
            dct[s[R]] = 1 + dct.get(s[R], 0)
            maxF = max(maxF, dct[s[R]])

            while (R - L + 1 - maxF) > k:
                dct[s[L]] -= 1
                L += 1
            
            maxLen = max(maxLen, R - L + 1)
        
        return maxLen