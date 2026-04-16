"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
"""
from collections import Counter


# Method 1: using 2 maps --> Time complexity: O(s+t) , Space Complexity: O(s+t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if the length is same
        if len(s) != len(t):
            return False

        # Iterate over staring and build maps
        s_count,t_count={},{}

        for ch in range(len(s)):

            s_count[s[ch]] = s_count.get(ch,0) + 1
            t_count[s[ch]] = t_count.get(ch, 0) +1

        # compare both the maps
        for ch in s_count:
            if s_count.get(ch,0) != t_count.get(ch,0):
                return False

        return True



s=Solution()
print('Are two strings anagram of each other?:', s.isAnagram("racecar","carrace"))


# Using Counter --> Time complexity: O(s+t) , Space Complexity: O(s+t)
s1='racecar'
t1='carrace'

result = (Counter(s1) == Counter(t1))
print('Given strings are anagram of each other?:', result)
