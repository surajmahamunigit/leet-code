# 11.01

class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """Find and return top k most frequent numbers in nums.

        Args:
            nums (list[int]): given list of integers
            k (int): top k most frequent numbers

        Returns:
              list[int]: op k most frequent numbers

        Time: O(n) - n = len(nums)

        Space: O(n)
        """

        # find frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # add the number and its frequency to frequency bucket -> index : number
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # read top k most frequent numbers and return
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return []

s = Solution()
print(s.top_k_frequent(nums = [1,2,2,3,3,3], k = 2))
print(s.top_k_frequent(nums = [7,7], k = 1))
print(s.top_k_frequent(nums=[], k=3))