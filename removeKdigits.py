""" 
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Constraints:

    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself. 
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return "".join(stack[:-k or None]).lstrip('0') or '0'  

print(Solution().removeKdigits("1432219", 3)) # "1219"
print(Solution().removeKdigits("10200", 1)) # "200"
print(Solution().removeKdigits("10", 2)) # "0"