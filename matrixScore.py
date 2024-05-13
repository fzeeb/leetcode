"""
You are given an m x n binary matrix grid.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score after making any number of moves (including zero moves).

Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Example 2:
Input: grid = [[0]]
Output: 1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 20
    grid[i][j] is either 0 or 1.
"""
from typing import List
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[i])):
                    grid[i][j] = 1 - grid[i][j]
        
        for j in range(1, len(grid[0])):
            count = sum(grid[i][j] for i in range(len(grid)))
            if count < len(grid) - count:
                for i in range(len(grid)):
                    grid[i][j] = 1 - grid[i][j]
        
        return sum(int("".join(map(str, row)), 2) for row in grid)
        

print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])) # 39
print(Solution().matrixScore([[0]])) # 1