"""
You are given an array nums of non-negative integers and an integer k.
An array is called special if the bitwise OR of all of its elements is at least k.
Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

Example 1:
Input: nums = [1,2,3], k = 2
Output: 1
Explanation:
The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:
Input: nums = [2,1,8], k = 10
Output: 3
Explanation:
The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:
Input: nums = [1,2], k = 0
Output: 1
Explanation:
The subarray [1] has OR value of 1. Hence, we return 1.

Constraints:
1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 10^9
0 <= k <= 10^9

Hint 1
For each nums[i], we can maintain each subarray’s bitwise OR result ending with it.

Hint 2
The property of bitwise OR is that it never unsets any bits and only sets new bits

Hint 3
So the number of different results for each nums[i] is at most the number of bits 32.
"""
from typing import List
class Solution:
    def minimumSubarrayLength(self, nums, k):
        min_length = float('inf')
        current_ors = {}
        
        for num in nums:
            new_ors = {}
            # Start a new subarray with num
            new_ors[num] = 1
            
            for or_value, length in current_ors.items():
                new_or = or_value | num
                new_length = length + 1
                if new_or in new_ors:
                    if new_length < new_ors[new_or]:
                        new_ors[new_or] = new_length
                else:
                    new_ors[new_or] = new_length
            
            # Update min_length if any OR value >= k
            for or_value, length in new_ors.items():
                if or_value >= k:
                    if length < min_length:
                        min_length = length
            
            current_ors = new_ors
        
        return -1 if min_length == float('inf') else min_length
    

# Test Cases
s = Solution()
print(s.minimumSubarrayLength([1,2,3], 2))  # Expected Output: 1
print(s.minimumSubarrayLength([2,1,8], 10))  # Expected Output: 3
print(s.minimumSubarrayLength([1,2], 0))  # Expected Output: 1