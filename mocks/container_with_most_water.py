# algorithm:
# given heights = [1,8,6,2,5,4,8,3,7]
# we use max_area= 0 and two pointers left and right. left = 0 and right = len(heights) - 1
# while left < right -> current_area = (right - left) * min(heights[left], heights[right]) ->
# then compare with max_area = max(max_area, current_area)
# if heights[left] <= heights[right] -> left += 1. else right -= 1
# in end return max_area

# example
# [1,8,6,2,5,4,8,3,7]
# left = 0, heights[left] = 1, right = 8, heights[right] = 7 -> current_are = (8-0) * 1 = 8
# left = 1, heights[left] = 8, right = 8, heights[right] = 7 -> current_are = (8-1) * 7 = 49
# left = 1, heights[left] = 8, right = 7, heights[right] = 3 -> current_are = (7-1) * 3 = 18
# left = 1, heights[left] = 8, right = 6, heights[right] = 8 -> current_are = (6-1) * 8 = 40

# left = 2, heights[left] = 6, right = 6, heights[right] = 8 -> current_are = (6-2) * 6 = 24
# left = 3, heights[left] = 2, right = 6, heights[right] = 8 -> current_are = (6-3) * 2 = 6
# left = 4, heights[left] = 5, right = 6, heights[right] = 8 -> current_are = (6-4) * 5 = 10
# left = 5, heights[left] = 4, right = 6, heights[right] = 8 -> current_are = (6-5) * 4 = 4
# left = 6, right = 6 -> max_area = 49

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        """Find two lines that form max water area to hold water.

         Args:
             heights: list containing lines height at heights[index]

         Returns:
             max area container we can form using two lines.

         Time: O(n) - n = len(heights)
         Space: O(1)
         """
        max_area = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, current_area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()
assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert s.maxArea([1,1]) == 1
print("passed")