"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.
A pair (i, j) is fair if:
0 <= i < j < n, and
lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

Constraints:
1 <= nums.length <= 10^5
nums.length == n
-10^9 <= nums[i] <= 10^9
-10^9 <= lower <= upper <= 10^9
"""
from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        answer = 0
        nums.sort()
        
        left = 0
        right = 1

        while left < n - 1:
            mid = nums[left] + nums[right]
            if 0 <= left and left < right and right < n and lower <= mid and mid <= upper:
                answer += 1
            if right < n - 1:
                right += 1
            else:
                left += 1
                right = left + 1


        return answer
    
# Test Cases
s = Solution()
print(s.countFairPairs([0,1,7,4,4,5], 3, 6)) # 6
print(s.countFairPairs([1,7,9,2,5], 11, 11)) # 1