class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        check = True

        while check:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                check = False

        slow_2 = 0
        check = True

        while check:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                check = False
        
        return slow