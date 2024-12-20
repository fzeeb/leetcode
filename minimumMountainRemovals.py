"""
You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

Example 1:
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.

Example 2:
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 
Constraints:
3 <= nums.length <= 1000
1 <= nums[i] <= 1^9
It is guaranteed that you can make a mountain array out of nums.

Hint 1
Think the opposite direction instead of minimum elements to remove the maximum mountain subsequence

Hint 2
Think of LIS it's kind of close
"""
from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # Calculate the length of the longest increasing subsequence ending at each index
        inc = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], inc[j] + 1)
        
        # Calculate the length of the longest decreasing subsequence starting at each index
        dec = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i], dec[j] + 1)
        
        # Find the maximum length of the mountain subsequence
        res = 0
        for i in range(1, n - 1):
            if inc[i] > 1 and dec[i] > 1:
                res = max(res, inc[i] + dec[i] - 1)
        
        # Calculate the minimum number of elements to remove
        return n - res
        
# Test cases
s = Solution()
print(s.minimumMountainRemovals([1,3,1]) == 0)
print(s.minimumMountainRemovals([2,1,1,5,6,2,3,1]) == 3)