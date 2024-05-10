"""
You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
Return the k^th smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j]. 

Example 1:
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

Example 2:
Input: arr = [1,7], k = 1
Output: [1,7]

Constraints:
    2 <= arr.length <= 1000
    1 <= arr[i] <= 3 * 10^4
    arr[0] == 1
    arr[i] is a prime number for i > 0.
    All the numbers of arr are unique and sorted in strictly increasing order.
    1 <= k <= arr.length * (arr.length - 1) / 2
"""
from typing import List
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def count_less_than_mid(mid: float) -> int:
            count = 0
            j = 1
            max_fraction = 0
            max_fraction_i = 0
            max_fraction_j = 0
            for i in range(len(arr)-1):
                while j < len(arr) and arr[i] > mid * arr[j]:
                    j += 1
                if j == len(arr):
                    break
                count += len(arr) - j
                if arr[i] / arr[j] > max_fraction:
                    max_fraction = arr[i] / arr[j]
                    max_fraction_i = i
                    max_fraction_j = j
            return count, max_fraction_i, max_fraction_j

        left = 0
        right = 1
        while right - left > 1e-9:
            mid = (left + right) / 2
            count, max_fraction_i, max_fraction_j = count_less_than_mid(mid)
            if count < k:
                left = mid
            else:
                answer = [arr[max_fraction_i], arr[max_fraction_j]]
                right = mid
        return answer
 
print(Solution().kthSmallestPrimeFraction([1,2,3,5], 3)) #[2,5]
print(Solution().kthSmallestPrimeFraction([1,7], 1)) #[1,7]