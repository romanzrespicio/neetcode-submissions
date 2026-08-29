class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dct_t = {}
        for c in t:
            dct_t[c] = dct_t.get(c, 0) + 1

        window = {}
        L = 0
        have, need = 0, len(dct_t)
        res, resLen = [], float('infinity')

        for R in range(len(s)):
            c = s[R]
            window[c] = 1 + window.get(c, 0)

            if c in dct_t and window[c] == dct_t[c]:
                have += 1
            
            while have == need:
                if (R - L) < resLen:
                    res = [L, R]
                    resLen = R - L
                
                window[s[L]] -= 1
                if s[L] in dct_t and window[s[L]] < dct_t[s[L]]:
                    have -= 1
                L += 1
        
        if resLen == float('inf'):
            return ""

        L, R = res
        return s[L:R + 1]