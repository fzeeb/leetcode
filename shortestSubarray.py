"""
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1], k = 1
Output: 1

Example 2:
Input: nums = [1,2], k = 4
Output: -1

Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
1 <= k <= 10^9
"""
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        min_length = n + 1
        queue = []
        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                min_length = min(min_length, i - queue.pop(0))
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        return min_length if min_length != n + 1 else -1
        

# Test Cases
s = Solution()
print(s.shortestSubarray([1], 1)) # 1
print(s.shortestSubarray([1,2], 4)) # -1
print(s.shortestSubarray([2,-1,2], 3)) # 3