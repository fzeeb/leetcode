"""
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

  t is a subsequence of the string s.
  The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

 

Constraints:

    1 <= s.length <= 10^5
    0 <= k <= 25
    s consists of lowercase English letters.
"""
class Solution:
  def longestIdealString(self, s: str, k: int) -> int:
    # dp[c] will store the length of the longest ideal subsequence ending with character c
    dp = [0] * 26
    
    for char in s:
        # Get the index of the character in the alphabet (0-based)
        idx = ord(char) - ord('a')
        # We start with the current best + 1 (self-extension)
        max_length = dp[idx] + 1
        
        # Check characters within the range defined by k
        for i in range(max(-k, -idx), min(k + 1, 26 - idx)):
            if 0 <= idx + i < 26:
                max_length = max(max_length, dp[idx + i] + 1)
        
        # Update the dp table for the current character
        dp[idx] = max(dp[idx], max_length)
    
    # The answer is the maximum value in the dp table
    return max(dp)

  
print(Solution().longestIdealString("acfgbd", 2)) #4
print(Solution().longestIdealString("abcd", 3)) #4
print(Solution().longestIdealString("jxhwaysa", 14)) #5