=begin
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Example 2:
Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

Example 3:
Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.

Constraints:
    1 <= s.length, t.length <= 10^5
    s and t consist only of lowercase English letters.

Hint 1
Find the longest prefix of t that is a subsequence of s.

Hint 2
Use two variables to keep track of your location in s and t. If the characters match, increment both variables. Otherwise, only increment the variable for s.

Hint 3
The remaining characters in t must be appended to the end of s.
=end
# @param {String} s
# @param {String} t
# @return {Integer}
def append_characters(s, t)
  i = 0
  j = 0
  while i < s.length && j < t.length
    if s[i] == t[j]
      j += 1
    end
    i += 1
  end
  t.length - j
end

puts append_characters("coaching", "coding") # 4
puts append_characters("abcde", "a") # 0
puts append_characters("z", "abcde") # 5