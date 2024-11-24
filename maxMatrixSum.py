"""
You are given an n x n integer matrix. You can do the following operation any number of times:
Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.
Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

Example 1:
Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.

Example 2:
Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 
Constraints:
n == matrix.length == matrix[i].length
2 <= n <= 250
-10^5 <= matrix[i][j] <= 10^5

Hint 1
Try to use the operation so that each row has only one negative number.

Hint 2
If you have only one negative element you cannot convert it to positive.
"""
from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        total_sum = 0 
        negative_count = 0
        min_abs_value = float('inf')

        for i in range(n):
            for j in range(n):
                value = matrix[i][j]
                total_sum += abs(value)

                if value < 0:
                    negative_count += 1
                
                min_abs_value = min(min_abs_value, abs(value))

        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum
        

# Test Cases
s = Solution()
print(s.maxMatrixSum([[1,-1],[-1,1]]))  # Expected: 4
print(s.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))  # Expected: 16
