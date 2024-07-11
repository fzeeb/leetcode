=begin
You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.

Example 1:
Input: s = "(abcd)"
Output: "dcba"

Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.

Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

Constraints:
    1 <= s.length <= 2000
    s only contains lower case English characters and parentheses.
    It is guaranteed that all parentheses are balanced.

Hint 1
Find all brackets in the string.

Hint 2
Does the order of the reverse matter ?

Hint 3
The order does not matter.
=end
# @param {String} s
# @return {String}
def reverse_parentheses(s)
  stack = []
  stack.push("")
  s.each_char do |char|
    if char == "("
      stack.push("")
    elsif char == ")"
      popped = stack.pop
      stack[-1] += popped.reverse
    else
      stack[-1] += char
    end
  end
  stack[0]
end

puts reverse_parentheses("(abcd)") == "dcba"
puts reverse_parentheses("(u(love)i)") == "iloveu"
puts reverse_parentheses("(ed(et(oc))el)") == "leetcode"