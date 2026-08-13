# 6.01

class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """Find and return top k most frequent numbers in nums.

        Args:
            nums: list of integers
            k: top k most frequent numbers in nums

        Returns:
            list of top k most frequent numbers in nums

        Time: O(n) - n = len(nums)
        Space: O(n)
        """

        # nums = [1,1,1,2,2,3], k = 2

        # count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add to frequency bucket list
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # read from highest frequency for k numbers
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)

                if len(res) == k:
                    return res

        return []

s = Solution()
res = s.top_k_frequent(nums = [1,1,1,2,2,3], k = 2)
print(res)

# 6.11 -> 10 min with solution.