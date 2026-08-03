# algorithm
# nums = [100,4,200,1,3,2]. given array is unsorted, ma_seqq_len = 0
# convert the given array to set for O(1) lookup -> sorted_nums
# for each number in sorted_nums, check if its previous number exit in the set,
# if not, length = 0, then check while number + length in set, increase length by 1 and compare with max_seq_len
# in end return max_seq_len

# example
# nums_set = {100,4,200,1,3,2}, max_seq_len = 0
# num = 100, no previous (99) in set, max_len_seq = 1
# num = 4,  previous (3) in set, skip
# num = 200, no previous (199) in set, max_len_seq = 1
# num = 1, no previous (0) in set, after while max_seq_len = 4
# num = 3,  previous (2) in set, skip
# num = 2,  previous (1) in set, skip
# max_seq_len=4

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """Find the length of longest consecutive sequence in given array.

        Args:
            nums: unsorted integer array

        Return :
            length of longest consecutive sequence in nums

        Time: O(n) - n - len(nums), while loop only touches each number at most once when number is part of the chain or starting of chain.
        Space: O(n) - for nums_set
        """

        max_seq_len = 0

        nums_set = set(nums)
        for num in nums_set:

            if num - 1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1

                max_seq_len = max(max_seq_len, length)
        return max_seq_len

s = Solution()
assert s.longestConsecutive(nums = [100,4,200,1,3,2]) == 4
assert s.longestConsecutive(nums = [1,2,3,4,5]) == 5
assert s.longestConsecutive(nums = [10,1,3,5]) == 1
assert s.longestConsecutive(nums = []) == 0
print("passed")
