class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni_nums = set(nums)

        if len(nums) == 0:
            return 0

        starts = []
        count = 1
        out = 0

        for i in uni_nums:
            count = 1
            if i - 1 in uni_nums:
                continue
            while i + 1 in uni_nums:
                count += 1
                i += 1
            if count > out:
                out = count
        
        return out


                