=begin
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Constraints:

    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself. 
=end
# @param {String} num
# @param {Integer} k
# @return {String}
def remove_kdigits(num, k)
  stack = []
  num = num.to_s
  i = 0
  while i < num.length
    while stack.length > 0 && k > 0 && stack[-1] > num[i]
      stack.pop
      k -= 1
    end
    stack.push(num[i])
    i += 1
  end
  while k > 0
    stack.pop
    k -= 1
  end
  result = stack.join('').sub(/^0+/, '')
  result.length > 0 ? result : '0'
end

# Test cases
puts remove_kdigits("1432219", 3) # Expected "1219"
puts remove_kdigits("10200", 1) # Expected "200"
puts remove_kdigits("10", 2) # Expected "0"