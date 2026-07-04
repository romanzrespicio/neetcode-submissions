class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1

                while k < l:

                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total < target:
                        k += 1
                        continue
                    elif total > target:
                        l -= 1
                        continue
                    elif (total == target) and ([nums[i], nums[j], nums[k], nums[l]] not in out):
                        out.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                        


        return out