class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1

        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])

        for num, cnt in dct.items():
            buckets[cnt].append(num)
        
        out = []
        for i in range(len(buckets)-1, 0, -1):
            if buckets[i] != []:
                out += buckets[i]
            if len(out) == k:
                break

        return out


        

        