"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
    0 <= num <= 108
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
      num_list = list(str(num))
      last = {int(x): i for i, x in enumerate(num_list)}

      for i, x in enumerate(num_list):
        for d in range(9, int(x), -1):
          if last.get(d, -1) > i:
            num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
            return int(''.join(num_list))
      
      return num
    
# Test cases
s = Solution()
print(s.maximumSwap(2736) == 7236)
print(s.maximumSwap(9973) == 9973)
print(s.maximumSwap(98368) == 98863)
print(s.maximumSwap(1993) == 9913)
