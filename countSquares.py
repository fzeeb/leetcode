"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 
Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        # Initialize the count of squares
        count = 0
        # Iterate over the matrix
        for i in range(rows):
            for j in range(cols):
                # If the element is 1
                if matrix[i][j] == 1:
                    # If the element is in the first row or first column
                    if i == 0 or j == 0:
                        count += 1
                    else:
                        # Get the minimum of the left, top and diagonal elements
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                        count += matrix[i][j]
        return count
        

# Test Cases
s = Solution()
print(s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]) == 15)
print(s.countSquares([[1,0,1],[1,1,0],[1,1,0]]) == 7)