"""
A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".

Constraints:
1 <= s.length <= 10^5
s consists only of lowercase English letters.

Hint 1
What's the optimal way to delete characters if three or more consecutive characters are equal?

Hint 2
If three or more consecutive characters are equal, keep two of them and delete the rest.
"""
class Solution:
  def makeFancyString(self, s: str) -> str:
    res = []
    count = 0
    for c in s:
      if res and c == res[-1]:
        count += 1
      else:
        count = 1

      if count < 3:
        res.append(c)

    return ''.join(res)

# Test Cases
solution = Solution()
print(solution.makeFancyString("leeetcode") == "leetcode")
print(solution.makeFancyString("aaabaaaa") == "aabaa")
print(solution.makeFancyString("aab") == "aab")  