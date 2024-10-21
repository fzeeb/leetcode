"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.
You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

Example 2:
Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].

Example 3:
Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.

Constraints:
    1 <= s.length <= 16
    s contains only lower case English letters.

Hint 1
Use a set to keep track of which substrings have been used already

Hint 2
Try each possible substring at every position and backtrack if a complete split is not possible
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        substrings = set()
        first = 0
        last = 1

        while last <= len(s):
            if s[first:last] not in substrings:
                substrings.add(s[first:last])
                first = last
                last = first + 1
            else:
                last += 1

        return len(substrings)
    
# Test Cases
s = Solution()
print(s.maxUniqueSplit("ababccc") == 5)
print(s.maxUniqueSplit("aba") == 2)
print(s.maxUniqueSplit("aa") == 1)
print(s.maxUniqueSplit("wwwzfvedwfvhsww") == 11)