"""
You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
Return the number of unoccupied cells that are not guarded.

Example 1:
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.

Example 2:
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:
1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.

Hint 1
Create a 2D array to represent the grid. Can you mark the tiles that can be seen by a guard?

Hint 2
Iterate over the guards, and for each of the 4 directions, advance the current tile and mark the tile. When should you stop advancing?
"""
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # create a 2d Grid from m and n
        grid = [[0] * n for _ in range(m)]

        # mark the guards and walls in the grid
        for x, y in guards:
            grid[x][y] = 1
        for x, y in walls:
            grid[x][y] = -1

        # get every position in the grid in the same row or column as a guard
        for x, y in guards:
            # Mark cells in the same row to the left of the guard
            for j in range(y - 1, -1, -1):
              if grid[x][j] == -1 or grid[x][j] == 1:
               break
              grid[x][j] = 2

            # Mark cells in the same row to the right of the guard
            for j in range(y + 1, n):
              if grid[x][j] == -1 or grid[x][j] == 1:
                break
              grid[x][j] = 2

            # Mark cells in the same column above the guard
            for i in range(x - 1, -1, -1):
              if grid[i][y] == -1 or grid[i][y] == 1:
                break
              grid[i][y] = 2

            # Mark cells in the same column below the guard
            for i in range(x + 1, m):
              if grid[i][y] == -1 or grid[i][y] == 1:
                break
              grid[i][y] = 2
                
        # count the number of unguarded positions
        return sum(1 for row in grid for cell in row if cell == 0)


# Test Cases
s = Solution()
print(s.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]))  # Expected: 7
print(s.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))  # Expected: 4