class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            dct[i] = dct.get(i, 0) + 1
        
        buckets = [0] * len(nums)

        for num, cnt in dct.items():
            if buckets[cnt-1] == 0:
                buckets[cnt-1] = [num]
            else:
                buckets[cnt-1].append(num)

        out = []
        for i in buckets[-1::-1]:
            if len(out) == k:
                break
            if i != 0:
                out += i
        
        return out