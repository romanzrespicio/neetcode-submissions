class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        
        top_k = sorted(dct.items(), key=lambda item: item[1], reverse = True)[0:k]
        top_k_keys = [i[0] for i in top_k]

        return top_k_keys