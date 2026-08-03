# algorithm
# given m*n matrix, consider it as flat array. left = 0, right = m*n - 1
# mid = (left + right) // 2, we will calculate row and column index for each number sing this mid index. row = mid//columns, column= mid%columns
# now binary search logic -> if mid_num==target, return True, else if mid_num < target -> left = mid+1, else right = mid+1
# if not found return False

# exmaple
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, left = 0, right=4*3 - 1= 11
# while left <= right:
# 0 < 11 -> mid = 5, row=1, column= 1, mid_num = matrix[row][column] = 11, 11>target -> right=mid-1
# left = 0, right = 4, mid=2, mid_num=matrix[0][2]=5 -> 5 > target -> right = mid-1= 1
# left = 0, right = 1, mid =0, mid_num = matrix[0][0]=1 -> 1<target -> left = mid+1=1
# left=right=1, mid=1, mid_num=matrix[0][1]=3 - 3 == target -> return True
# in end return False

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """Find target number exists in m*n matrix array or not.

        Args:
            matrix: m*n matrix array
            target: target integer

        Returns:
            True if target number found, else False

        Time: O(log m*n) - m, n = dimensions of matrix
        Space: O(1)
        """
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left+right)//2
            row = mid // len(matrix[0])
            column = mid % len(matrix[0])
            mid_num = matrix[row][column]

            if mid_num == target:
                return True
            elif mid_num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

s = Solution()
assert s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3) == True
assert s.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13) == False
print("passed")