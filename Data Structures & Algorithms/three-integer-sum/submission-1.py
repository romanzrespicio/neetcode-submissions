class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums) - 2):

            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif [nums[i], nums[j], nums[k]] not in out:
                    out.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    j += 1
                else:
                    k -= 1
                    j += 1
            
        return out
        