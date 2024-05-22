"""
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s. 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        def dfs(i, path):
            if i == len(s):
                res.append(path)
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    dfs(j + 1, path + [s[i:j+1]])
        res = []
        dfs(0, [])
        return res

print(Solution().partition("aab")) # [["a","a","b"],["aa","b"]]
print(Solution().partition("a")) # [["a"]]