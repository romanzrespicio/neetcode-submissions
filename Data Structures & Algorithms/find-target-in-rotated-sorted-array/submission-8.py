class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        pivot = l

        def BS(left, right, target):

            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    right = m - 1
                else:
                    left = m + 1
            
            return -1

        res = BS(0, pivot - 1, target)

        if res != -1:
            return res

        res = BS(pivot, len(nums) - 1, target)

        return res