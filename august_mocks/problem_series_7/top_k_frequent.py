# 12.28
# given list of integers and asked to return top k most freq. numbers

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find and return top k most frequent number sin given array.

        Args:
            nums: integer array
            k: number of top frequent numbers

        Returns:
            top k most frequent numbers

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        # count the frequency of given numbers
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add to frequency bucket as frequency -> number
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # read top k
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return []

s = Solution()
assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]
assert s.topKFrequent([-1,-1,-2,-2,-2], 1) == [-2]
print("passed")

# 12.37 -> 9 min to solve