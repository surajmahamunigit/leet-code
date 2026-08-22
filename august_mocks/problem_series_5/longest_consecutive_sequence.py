# 12.18
# given an unsorted array of integers and asked to find longest consecutive sequence
# meaning 1,2,3,4, whatever sequence possible in given array
# for every number in array -> check if that numbers previous number s in array -> yes -> skip
# no -> start counting length from this number until sequential numbers are available in array and compare with max_length

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Find length of longest consecutive sequence in given array.

        Args:
            nums: unsorted integer array

        Returns:
            length of longest consecutive sequence in given array

        Time: O(n) - n = len(nums)
        Space: O(n)
        """
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 in nums_set:
                continue

            length = 0
            while num + length in nums_set:
                length += 1
                longest = max(length, longest)

        return longest

s = Solution()
assert s.longestConsecutive([100,4,200,1,3,2]) == 4
assert s.longestConsecutive([1,2,3,4,5]) == 5
assert s.longestConsecutive([10,1,3,5]) == 1
assert s.longestConsecutive([]) == 0
print("passed")

# 12.25 -> 7 min to solve