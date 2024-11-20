"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:
1 <= s.length <= 10^5
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length

Hint 1
Start by counting the frequency of each character and checking if it is possible.

Hint 2
If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.

Hint 3
Use a two-pointers approach to avoid computing the same information multiple times.
"""
from math import inf

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if s.count('a') < k or s.count('b') < k or s.count('c') < k:
            return -1

        n = len(s)
        left = 0
        right = n - 1
        result = float(inf)

        while left <= n:
            tmp_str = s[0:left] + s[right:n]
            print(tmp_str)
            if tmp_str.count('a') >= k and tmp_str.count('b') >= k and tmp_str.count('c') >= k:
                result = min(result, len(tmp_str))
                left += 1
                right = n - 1
            
            right -= 1


        return result


# Test Cases
s = Solution()
print(s.takeCharacters("aabaaaacaabc", 2)) # 8
print(s.takeCharacters("a", 1)) # -1