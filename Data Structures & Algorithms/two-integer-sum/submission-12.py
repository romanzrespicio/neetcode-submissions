class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dct = {}
        for i in range(len(nums)):
            dct[nums[i]] = i


        for i in range(len(nums)):
            diff = target - nums[i] 
            if (diff in dct) and (dct[diff] != i):
                return [i, dct[diff]]
            

