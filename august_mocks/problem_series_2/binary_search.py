# 4..02
# given sorted array and asked to find target else -1
# binary search pattern

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Find the target number in given sorted array and return its index, else return -1.

        Args:
            nums: sorted array
            target: number to look for

        Returns:
            index of target number if found, else -1

        Time: O(log n) - n = len(nums)
        Space: O(1)
        """

        left = 0
        right = len(nums) - 1

        while left <= right:
            index = (left + right) // 2
            val = nums[index]

            if val < target:
                left = index + 1
            elif val > target:
                right = index - 1
            else:
                return index

        return - 1

s = Solution()
assert s.search([-1,0,3,5,9,12], 9) == 4
assert s.search([-1,0,3,5,9,12], 2) == -1
assert s.search([-1,0,3,5,9,12], 22) == -1
assert s.search([-1,0,3,5,9,12], -2) == -1
assert s.search([-1], -1) == 0
assert s.search([-1], 1) == -1
print("passed")

# 4.12 -> 10 min to solve