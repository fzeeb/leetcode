=begin
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
=end
# @param {String} s
# @return {Integer}
def longest_palindrome(s)
  hash = Hash.new(0)
  s.each_char do |c|
    hash[c] += 1
  end
  odd = 0
  hash.each do |k, v|
    odd += 1 if v.odd?
  end
  return s.length - odd + (odd > 0 ? 1 : 0)
end

puts longest_palindrome("abccccdd") # 7
puts longest_palindrome("a") # 1