"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].

Example 2:
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].

Example 3:
Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 
Constraints:
1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9

Hint 1
The key is to find the longest non-decreasing subarray starting with the first element or ending with the last element, respectively.

Hint 2
After removing some subarray, the result is the concatenation of a sorted prefix and a sorted suffix, where the last element of the prefix is smaller than the first element of the suffix.
"""
from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)

        if arr == sorted(arr):
            return 0

        if arr == sorted(arr, reverse=True):
            return n-1

        remove = []

        for i in range(0, n-1):
            if arr[i] > arr[i+1]:
                remove.append(arr[i])
                remove.append(arr[i+1])
        
        return len(set(remove))
    
# Test cases
s = Solution()
print(s.findLengthOfShortestSubarray([1,2,3,10,4,2,3,5])) # 3
print(s.findLengthOfShortestSubarray([5,4,3,2,1])) # 4
print(s.findLengthOfShortestSubarray([1,2,3])) # 0