#  algorithm
# given is integer array with duplicates numbers and we have to return top k most repeated numbers
# first for every number in nums, count its freq and use dict to store it num_freq as num-> freq
# then use array size = len(nums)+1.  use the arrays index as freq of number and add num to that index called it bucket.
# in end read array backwards from last index until we get k numbers and then return it

# example
# nums = [1,2,2,3,3,3], k = 2
# num_freq = {1:1, 2:2, 3:3}
# bucket = [0,1,2,3]
# top-k = [3,2]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find top k most repeated numbers in given integer array.

        Args:
            nums: integer array with duplicates
            k: top k frequent numbers

        Returns:
            list of top k most frequent numbers in nums.

        Time: O(n^2) - n = len(nums)
        Space: O(n)
        """
        result = []
        # find the numbers frequency
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)

        # add to the freq bucket
        bucket = [ [] for _ in range(len(nums) + 1)]
        for num, freq in num_freq.items():
            bucket[freq].append(num)

        # read from backwards and add number to result until its k
        for index in range(len(bucket)-1, 0, -1):
            for num in bucket[index]:
                result.append(num)
                if len(result) == k:
                    return result

        return []

s = Solution()
assert s.topKFrequent(nums = [1,2,2,3,3,3], k = 2) == [3,2]
assert s.topKFrequent(nums = [7,7], k=1) == [7]
assert s.topKFrequent([],1) == []
print("passed")