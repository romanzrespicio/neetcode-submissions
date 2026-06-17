class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        if len(nums) == 0:
            return res

        if len(nums) == 1:
            return [0]

        zeroidx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                break
            zeroidx += 1
        
        prev = 1
        for i in nums[0:zeroidx]:
            prev *= i
        for i in nums[zeroidx+1:]:
            prev *= i
        
        if prev == 0:
            return [0] * len(nums)
        elif zeroidx != len(nums):
            res = [0] * len(nums)
            res[zeroidx] = prev
            return res

        prev = 1
        for i in range(1, len(nums)):
            prev *= nums[i]
        res.append(prev)
        
        for i in range(1, len(nums)):
            if nums[i] != 0:
                prev = prev / nums[i]
            prev = prev * nums[i-1]
            res.append(int(prev))
        
        return res

        