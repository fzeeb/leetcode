"""
You are given two strings s and t of the same length and an integer maxCost.
You want to change s to t. Changing the i^th character of s to i^th character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).
Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.

Constraints:
    1 <= s.length <= 10^5
    t.length == s.length
    0 <= maxCost <= 10^6
    s and t consist of only lowercase English letters.

Hint 1
Calculate the differences between a[i] and b[i].

Hint 2
Use a sliding window to track the longest valid substring.
"""
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        start = 0
        end = 0
        total = 0
        max_len = 0
        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            max_len = max(max_len, end - start + 1)
            end += 1
        return max_len
    
print (Solution().equalSubstring("abcd", "bcdf", 3)) # 3
print (Solution().equalSubstring("abcd", "cdef", 3)) # 1
print (Solution().equalSubstring("abcd", "acde", 0)) # 1