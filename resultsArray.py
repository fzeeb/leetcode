"""
You are given an array of integers nums of length n and a positive integer k.
The power of an array is defined as:
Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.
Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.

Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]

Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]

Constraints:
1 <= n == nums.length <= 500
1 <= nums[i] <= 10^5
1 <= k <= n

Hint 1
Can we use a brute force solution with nested loops and HashSet?
"""
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            # Check if subarray is strictly increasing
            is_sorted = all(subarray[j] < subarray[j + 1] for j in range(k - 1))
            # Check if difference between max and min is k-1
            if is_sorted and max(subarray) - min(subarray) == k - 1:
                results.append(subarray[-1])
            else:
                results.append(-1)
                
        return results
        

# Test Cases
s = Solution()
print(s.resultsArray([1,2,3,4,3,2,5], 3)) # [3,4,-1,-1,-1]
print(s.resultsArray([2,2,2,2,2], 4)) # [-1,-1]
print(s.resultsArray([3,2,3,2,3,2], 2)) # [-1,3,-1,3,-1]
print(s.resultsArray([1,2,2,4,2], 4)) # [-1,-1]