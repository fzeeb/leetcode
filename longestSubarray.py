"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9

Hint 1
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.

Hint 2
More specifically, use the two pointer technique, moving the right pointer as far as possible to the right until the subarray is not valid (maxValue - minValue > limit), then moving the left pointer until the subarray is valid again (maxValue - minValue <= limit). Keep repeating this process.
"""
from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()
        mind = deque()
        left = 0
        for right, num in enumerate(nums):
            while maxd and num > maxd[-1]:
                maxd.pop()
            while mind and num < mind[-1]:
                mind.pop()
            maxd.append(num)
            mind.append(num)
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[left]:
                    maxd.popleft()
                if mind[0] == nums[left]:
                    mind.popleft()
                left += 1
        return right - left + 1   

print(Solution().longestSubarray([8,2,4,7], 4)) # 2
print(Solution().longestSubarray([10,1,2,4,7,2], 5)) # 4
print(Solution().longestSubarray([4,2,2,2,4,4,2,2], 0)) # 3