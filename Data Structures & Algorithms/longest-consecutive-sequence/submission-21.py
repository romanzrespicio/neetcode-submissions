class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uni_nums = set(nums)

        starts = []
        for num in uni_nums:
            if num - 1 not in uni_nums:
                starts.append(num)
        
        longest = 0
        for start in starts:
            length = 1
            while start + length in uni_nums:
                length += 1
            
            longest = max(longest, length)
        
        return longest