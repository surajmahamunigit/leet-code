# 8.44

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find top k most frequent numbers from the given array.

        Args:
            nums (list[int]): list of integers
            k (int): most frequent k integers

        Returns:
             list[int]: list of top k most frequent numbers

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        result = []

        # count the frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add to frequency bucket lists
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # get top k numbers
        for freq in range(len(buckets)-1, 0, - 1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return result

s = Solution()
assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]
assert s.topKFrequent([-1,-1,-2,-2,-2], 1) == [-2]
print('passed')