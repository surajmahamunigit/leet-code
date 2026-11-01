# 12.22
from collections import defaultdict

class Solution:
    def top_k_elements(self, nums: list[int], k: int) -> list[int]:
        """Find and return top k elements in given integer array.

        Args:
            nums (list[int]): integer array
            k (int): top most frequent elements in given array

        Returns:
             list[int]: list of top k most frequent elements in given array

        Time complexity: O(n) - n = len(nums)

        Space complexity: O(n)
        """

        # count the numbers frequency
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # add num and frequency to bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            bucket[freq].append(num)

        # read top k elements and return
        result = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return []

s = Solution()

def check(values, k, expected):
    result = s.top_k_elements(values, k)
    assert result == expected

check([1,2,2,3,3,3], 2, [3,2])
check([3,3], 1, [3])
check([1,2,3], 1,[1])
check([1], 1, [1])
print("all tests passed")

# 12.39 -> 17 minutes to solve
# git commit -> feat: add top k elements solution