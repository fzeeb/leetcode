=begin
Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.

Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.
=end
# @param {Integer} n
# @return {Integer}
def pivot_integer(n)
  right_sum = (1..n).sum
  left_sum = 0

  (n).downto(1) do |i|
    left_sum += i
    return i if left_sum == right_sum
    right_sum = right_sum - i
  end

  -1
end

puts pivot_integer(8) # 6