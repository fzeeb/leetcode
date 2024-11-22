"""
You are given an m x n binary matrix matrix.
You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).
Return the maximum number of rows that have all values equal after some number of flips.

Example 1:
Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:
Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:
Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.

Hint 1
Flipping a subset of columns is like doing a bitwise XOR of some number K onto each row. We want rows X with X ^ K = all 0s or all 1s. This is the same as X = X^K ^K = (all 0s or all 1s) ^ K, so we want to count rows that have opposite bits set. For example, if K = 1, then we count rows X = (00000...001, or 1111....110).
"""
from collections import Counter
from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = Counter()
        
        for row in matrix:
            # Normalize each row so that the first value is 0
            # If the first value is 1, flip the entire row
            normalized_row = tuple(cell ^ row[0] for cell in row)
            pattern_count[normalized_row] += 1
        
        # The maximum count of any pattern
        return max(pattern_count.values())
        
        
# Test Cases
s = Solution()
print(s.maxEqualRowsAfterFlips([[0,1],[1,1]]))  # Expected: 1
print(s.maxEqualRowsAfterFlips([[0,1],[1,0]]))  # Expected: 2
print(s.maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]]))  # Expected: 2