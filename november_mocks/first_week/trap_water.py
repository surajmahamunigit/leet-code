# 8.20

class Solution:
    def trap(self, height: list[int]) -> int:
        """Find the total water trapped.

         Args:
             height (list[int]): list of integers representing each bars height

         Returns:
             int: total water trapped

         Time complexity: O(n) - n = len(height)

         Space complexity: O(1)
         """

        water_trapped = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]

        while left < right:

            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water_trapped += (left_max - height[left])
                left += 1
            else:
                right_max = max(right_max, height[right])
                water_trapped += (right_max - height[right])
                right -= 1

        return water_trapped

s = Solution()

def check(values, expected):
    result = s.trap(values)
    assert result == expected

check([0,0,0,0], 0)
check([1,2,3], 0)
check([3,2,1], 0)
check([0,1,0,3], 1)
check([0,2,0,3,1,0,1,3,2,1], 9)
check([2,0,4,6,0],2)
print("all tests passed")


