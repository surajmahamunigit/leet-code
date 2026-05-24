"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Time: O(n*2)
Space: O(n)

"""

class Solution:
    def threeSum(self, numbers: list[int]) -> list[list[int]]:

        result = []
        numbers.sort()

        for index, num in enumerate(numbers):

            if index > 0 and num == numbers[index - 1]:
                continue

            # Use two pointer problem strategy

            left_index = index+1
            right_index = len(numbers) -1

            while left_index < right_index:

                total_sum = num + numbers[left_index] + numbers[right_index]

                if total_sum > 0:
                    right_index -= 1

                elif total_sum < 0:
                    left_index += 1

                else:
                    result.append([num, numbers[left_index], numbers[right_index]])

                    left_index += 1

                    while left_index < right_index and numbers[left_index] == numbers[left_index - 1]:
                        left_index += 1

        return result



result = Solution().threeSum([-1,0,1,2,-1,-4])
print(result)
