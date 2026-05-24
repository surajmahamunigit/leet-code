"""
You are given an integer array heights where heights[i] represents the height of the i'th  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]

Output: 36

Time: O(n)
Space: O(1)
"""
class Solution:
    def maxArea(self, heights:list[int]) -> int:

        result = 0


        # Two pointer problem approach
        left_index = 0
        right_index = len(heights) - 1

        while left_index < right_index:
            area = (right_index - left_index) * min(heights[left_index], heights[right_index])
            result = max(result, area)

            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return result



        # #   BRUTE FORCE
        # for left in range(len(heights)-1):
        #     for right in range(left+1, len(heights)):
        #         area = (right - left) * min(heights[left], heights[right])
        #         result = max(result, area)
        #
        # return result

result = Solution().maxArea([1,7,2,5,4,7,3,6])
print(result)