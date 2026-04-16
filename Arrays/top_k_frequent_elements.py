"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
"""


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        print(f'Given Array: {nums}')

        # Count the frequency of each element in the array
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        print(count)  # {1: 3, 2: 2, 3: 1}

        # add in the bucket index=count for each element
        freq = [[] for i in range(len(nums) + 1)]

        for num,count in count.items():
            freq[count].append(num)
        print(freq)  # [[], [3], [2], [1], [], [], []]


        # return k frequent elements in array
        res=[]

        for i in range(len(freq)-1,0,-1):  # For every list inside the list starting from end to 0


            for num in freq[i]:    # for every num in list
                res.append(num)

                # Everytime check if len(result-array) == k or not
                if len(res)==k:
                    return res

        return None


s=Solution()
result=s.topKFrequent([1,2,1,1,2,3],2)
print(result)