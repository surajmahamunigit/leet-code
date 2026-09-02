# 5.38

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find top k most frequent numbers in given array.

        Args:
            nums: integer array
            k: most frequent numbers

        Returns:
            list of top k most frequent numbers

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        # [1,2,3,4,5,1,2]
        result = []

        # count the frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add numbers to frequency bucket
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # get top k

        for freq  in range(len(buckets) - 1, 0, -1):
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