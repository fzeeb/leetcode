=begin
You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.

Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.

Constraints:
    1 <= s.length <= 10^5
    s[i] is 'a' or 'b'​​.

Hint 1
You need to find for every index the number of Bs before it and the number of A's after it

Hint 2
You can speed up the finding of A's and B's in suffix and prefix using preprocessing
=end
# @param {String} s
# @return {Integer}
def minimum_deletions(s)
  n = s.size
  a_count = Array.new(n+1, 0)
  b_count = Array.new(n+1, 0)
  count = 0

  (1..n).each do |i|
    a_count[i] = a_count[i-1]
    b_count[i] = b_count[i-1]

    if s[i-1] == "a"
      a_count[i] += 1
    else
      b_count[i] += 1
    end
  end

  (0..n).each do |i|
    count = [count, a_count[i] + b_count[n] - b_count[i]].max
  end

  n - count 
end

# Test cases
puts minimum_deletions("aababbab") == 2
puts minimum_deletions("bbaaaaabb") == 2