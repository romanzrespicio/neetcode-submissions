class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowID = -1

        for row in range(len(matrix)):
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                rowID = row
                break

        if rowID == -1:
            return False
        
        l = 0
        r = len(matrix[rowID]) - 1
        nums = matrix[rowID]

        while l <= r:
            
            mid = (l + r) // 2

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                print(nums[mid])
                return True

        return False
        