"""
You are given a 0-indexed m x n matrix grid consisting of positive integers.
You can start at any cell in the first column of the matrix, and traverse the grid in the following way:
From a cell (row, col), you can move to any of the cells: (row - 1, col + 1), (row, col + 1) and (row + 1, col + 1) such that the value of the cell you move to, should be strictly bigger than the value of the current cell.
Return the maximum number of moves that you can perform.

Example 1:
Input: grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
Output: 3
Explanation: We can start at the cell (0, 0) and make the following moves:
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
It can be shown that it is the maximum number of moves that can be made.

Example 2:
Input: grid = [[3,2,4],[2,1,9],[1,1,7]]
Output: 0
Explanation: Starting from any cell in the first column we cannot perform any moves.
 
Constraints:
m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 10^5
1 <= grid[i][j] <= 10^6

Hint 1
Consider using dynamic programming to find the maximum number of moves that can be made from each cell.

Hint 2
The final answer will be the maximum value in cells of the first column.
"""
from typing import List
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
      m, n = len(grid), len(grid[0])
      dp = [[0] * n for _ in range(m)]
      
      # Traverse the grid from the last column to the first column
      for col in range(n - 2, -1, -1):
          for row in range(m):
              # Check all three possible moves: (row-1, col+1), (row, col+1), (row+1, col+1)
              for dr in [-1, 0, 1]:
                  nr, nc = row + dr, col + 1
                  # Ensure the new row and column are within bounds
                  if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[row][col]:
                      dp[row][col] = max(dp[row][col], dp[nr][nc] + 1)

      # The answer is the maximum moves starting from any cell in the first column
      return max(dp[row][0] for row in range(m))
    
# Test cases
s = Solution()
print(s.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]) == 3)
print(s.maxMoves([[3,2,4],[2,1,9],[1,1,7]]) == 0)