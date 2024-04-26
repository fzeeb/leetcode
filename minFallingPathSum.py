from typing import List
"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.

Example 2:

Input: grid = [[7]]
Output: 7

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""
class Solution:
  def minFallingPathSum(self, grid: List[List[int]]) -> int:
      n = len(grid)
      if n == 1:
          return grid[0][0]
      
      # Initialize the dp array with the values of the first row
      dp = [[0] * n for _ in range(n)]
      dp[0] = grid[0][:]
      
      # Fill the dp array
      for i in range(1, n):
          # Get the smallest and second smallest values from the previous row
          # Initialize min1 and min2 to infinity
          min1, min2 = float('inf'), float('inf')
          idx1 = -1
          
          for j in range(n):
              if dp[i-1][j] < min1:
                  min2 = min1
                  min1 = dp[i-1][j]
                  idx1 = j
              elif dp[i-1][j] < min2:
                  min2 = dp[i-1][j]
                  
          # Update the current row values in dp
          for j in range(n):
              if j == idx1:
                  dp[i][j] = grid[i][j] + min2
              else:
                  dp[i][j] = grid[i][j] + min1
      
      # The answer is the minimum value in the last row of dp
      return min(dp[n-1])
  
print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])) # 13
print(Solution().minFallingPathSum([[7]])) # 7