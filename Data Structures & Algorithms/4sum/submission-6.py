class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Adjacent check with edge case check
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):
                # Adjacent check with edge case check
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                k, l = j+1, n-1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        out.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        # Adjacent check with edge case check (for duplicates)
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
        return out