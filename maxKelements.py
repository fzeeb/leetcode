from math import ceil
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        l = len(nums) - 1
        while k > 0:
            nums.sort()
            score += nums[l]
            nums[l] = ceil(nums[l] / 3)
            k -= 1
        
        return score
    
# Test cases
s = Solution()
print(s.maxKelements([10,10,10,10,10], 5) == 50)
print(s.maxKelements([1,10,3,3,3], 3) == 17)