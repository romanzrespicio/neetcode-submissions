class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c) - ord('a')] += 1

            key = str(lst)
            if key in dct:
                dct[key] += [s]
            else:
                dct[key] = [s]
        
        return list(dct.values())


        


        