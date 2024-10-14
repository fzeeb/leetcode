from math import ceil
from typing import List
import heapq

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        while k > 0:
            max_value = -heapq.heappop(max_heap)
            score += max_value

            heapq.heappush(max_heap, -ceil(max_value / 3))

            k -= 1
        
        return score
    
# Test cases
s = Solution()
print(s.maxKelements([10,10,10,10,10], 5) == 50)
print(s.maxKelements([1,10,3,3,3], 3) == 17)