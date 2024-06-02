=begin
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
    1 <= s.length <= 105
    s[i] is a printable ascii character.

Hint 1
The entire logic for reversing a string is based on using the opposite directional two-pointer approach!
=end
# @param {Character[]} s
# @return {Void} Do not return anything, modify s in-place instead.
def reverse_string(s)
  left = 0
  right = s.length - 1
  while left < right
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
  end
  s
end

print reverse_string(["h", "e", "l", "l", "o"]) # ["o", "l", "l", "e", "h"]
print reverse_string(["H", "a", "n", "n", "a", "h"]) # ["h", "a", "n", "n", "a", "H"]