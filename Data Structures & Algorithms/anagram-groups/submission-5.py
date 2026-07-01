class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for s in strs:
            arr = [0] * 26
            
            for c in s:
                idx = ord(c) - ord('a')
                arr[idx] += 1
            
            arr_key = tuple(arr)

            if arr_key in dct:
                dct[arr_key].append(s)
            else:
                dct[arr_key] = [s]

        return list(dct.values())


        