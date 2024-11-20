"""
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions

Example 2:
Input: nums = [4,4,4], k = 3
Output: 0
Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 
Constraints:
1 <= k <= nums.length <= 10^5
1 <= nums[i] <= 10^5

Hint 1
Which elements change when moving from the subarray of size k that ends at index i to the subarray of size k that ends at index i + 1?

Hint 2
Only two elements change, the element at i + 1 is added into the subarray, and the element at i - k + 1 gets removed from the subarray.

Hint 3
Iterate through each subarray of size k and keep track of the sum of the subarray and the frequency of each element.
"""
from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0

        # Hash map to store the frequency of elements in the current window
        freq = defaultdict(int)
        window_sum = 0
        max_sum = 0
        
        for i in range(n):
            # Add the new element to the window
            window_sum += nums[i]
            freq[nums[i]] += 1

            # If the window size exceeds k, remove the oldest element
            if i >= k:
                window_sum -= nums[i - k]
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]] == 0:
                    del freq[nums[i - k]]

            # Check if the window is valid and update max_sum
            if i >= k - 1 and len(freq) == k:  # Valid window has k distinct elements
                max_sum = max(max_sum, window_sum)

        return max_sum

# Test Cases
s = Solution()
print(s.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))  # 15
print(s.maximumSubarraySum([4, 4, 4], 3))  # 0
print(s.maximumSubarraySum([1, 2, 3, 4, 5], 3))  # 12