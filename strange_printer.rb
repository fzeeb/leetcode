=begin
There is a strange printer with the following two special properties:
    The printer can only print a sequence of the same character each time.
    At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

Example 1:
Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Example 2:
Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.

Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters.
=end
# @param {String} s
# @return {Integer}
def strange_printer(s)
  n = s.length
  dp = Array.new(n + 1) { Array.new(n + 1, 0) }
  
  (0...n).each do |i|
    dp[i][i] = 1
  end
  
  (1...n).each do |len|
    (0...n - len).each do |i|
      j = i + len
      dp[i][j] = dp[i + 1][j] + 1
      (i + 1..j).each do |k|
        if s[i] == s[k]
          dp[i][j] = [dp[i][j], dp[i][k - 1] + dp[k + 1][j]].min
        end
      end
    end
  end

  dp[0][n - 1]  
end

# Test cases
puts strange_printer("aaabbb") == 2
puts strange_printer("aba") == 2