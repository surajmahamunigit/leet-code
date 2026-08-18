# 5.12

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """Find top k most frequent numbers in list.

        Args:
            nums: list of integers
            k: top k most frequent numbers

        Returns:
            list of top k most frequent numbers

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        # count number freq
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add to the freq bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)

        # read bucket in reverse order
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return []

s = Solution()
assert s.topKFrequent([1,1,1,2,2,3], 2) == [1,2]
assert s.topKFrequent([1], 1) == [1]
assert s.topKFrequent([-1,-1,-2,-2,-2], 1) == [-2]
print("passed")

# 5.20 -> 8 min to solve