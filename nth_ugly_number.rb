=begin
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
    1 <= n <= 1690

Hint 1
The naive approach is to call isUgly for every number until you reach the n^th one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.

Hint 2
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

Hint 3
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L_1, L_2, and L_3.

Hint 4
Assume you have U_k, the k^th ugly number. Then U_k+1 must be Min(L_1 * 2, L_2 * 3, L_3 * 5).
=end
# @param {Integer} n
# @return {Integer}
def nth_ugly_number(n)
  ugly_numbers = [1]
  i2 = i3 = i5 = 0

  while ugly_numbers.length < n
    next_ugly = [ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5].min
    ugly_numbers << next_ugly

    i2 += 1 if next_ugly == ugly_numbers[i2] * 2
    i3 += 1 if next_ugly == ugly_numbers[i3] * 3
    i5 += 1 if next_ugly == ugly_numbers[i5] * 5
  end

  ugly_numbers.last  
end

# Test cases
puts nth_ugly_number(10) == 12
puts nth_ugly_number(1) == 1