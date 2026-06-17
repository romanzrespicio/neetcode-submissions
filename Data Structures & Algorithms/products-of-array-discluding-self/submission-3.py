class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 0:
            return []


        prod = nums[0]
        out = []

        for i in range(1, len(nums)):
            prod *= nums[i]

        if prod == 0:
            num_zeros = 0

            for i in range(len(nums)):
                if nums[i] == 0:
                    idx = i
                    num_zeros += 1
            
            if num_zeros > 1:
                return [0] * len(nums)
            
            prod = 1
            for i in range(len(nums)):
                if i == idx:
                    continue
                prod *= nums[i]
            
            out = [0] * len(nums)
            out[idx] = prod
            return out
    
        
        for i in range(len(nums)):
            out.append(int(prod / nums[i]))
        
        return out