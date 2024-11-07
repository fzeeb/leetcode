"""
The bitwise AND of an array nums is the bitwise AND of all integers in nums.
For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
Also, for nums = [7], the bitwise AND is 7.
You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.
Return the size of the largest combination of candidates with a bitwise AND greater than 0.

Example 1:
Input: candidates = [16,17,71,62,12,24,14]
Output: 4
Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
The size of the combination is 4.
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
Note that more than one combination may have the largest size.
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

Example 2:
Input: candidates = [8,8]
Output: 2
Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
The size of the combination is 2, so we return 2.
 
Constraints:
1 <= candidates.length <= 10^5
1 <= candidates[i] <= 10^7
"""
from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        # Iterate over each bit position (0 to 31 for 32-bit integers)
        for bit in range(32):
            count = 0
            for candidate in candidates:
                if candidate & (1 << bit):
                    count += 1
            max_count = max(max_count, count)
        return max_count
        
# Test Cases
s = Solution()
print(s.largestCombination([16,17,71,62,12,24,14]) == 4)
print(s.largestCombination([8,8]) == 2) 
print(s.largestCombination([13,44,58,17,23,13,87,79,91,47,86,90,4,93,18,75,29,66,43,60,19,3,28]) == 14) 
