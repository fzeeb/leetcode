=begin
Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Constraints:
    0 <= c <= 2^31 - 1
=end
# @param {Integer} c
# @return {Boolean}
def judge_square_sum(c)
  (0..Math.sqrt(c).to_i).each do |i|
    b = Math.sqrt(c - i * i)
    return true if b == b.to_i
  end
  false
end

puts judge_square_sum(5) # true
puts judge_square_sum(3) # false