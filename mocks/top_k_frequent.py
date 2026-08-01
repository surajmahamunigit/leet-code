# Algorithm
# given input array nums = [1,1,1,2,2,3]
# first cont the occurrence of each number in given array and store than in map as num : frequency -> {1:3, 2:1, 3:1}
# then add number: frequency in frequency bucket. bucket length = len(nums) + 1. use frequency as index of bucket and add number to that index
# [[],[3],[2],[1]]
# read the k numbers starting from highest index of bucket until numbers == k. then return list of top k numbers

# example:
# nums=[1,1,1,2,2,3], k = 1
# frequency count: {1:3, 2:1, 3:1}
# add to frequency bucket: [[],[3],[2],[1]]
# read from highest frequency index until numbers == k -> return [1]


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find top k numbers in given array.

        Args:
            nums: array of integers
            k : top k numbers

        Returns:
            top k most frequent numbers

        Time: O(n) -
        Space: O(n) - n = len(nums)
        """

        result = []

        # count the number frequency
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # add to the frequency bucket
        buckets = [[] for _ in range(len(nums) + 1)]        # counts 0 frequency
        for num, freq in count.items():
            buckets[freq].append(num)

        # read top k starting from highest index
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result

s = Solution()
assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]
print("passed")
