class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        pivot = l

        def binary_search(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return -1
        
        res = binary_search(nums[0:pivot], target)
        if res != -1:
            return res
        
        res = binary_search(nums[pivot:len(nums)], target)
        return pivot + res if res != -1 else -1