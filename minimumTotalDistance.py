"""
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [position_j, limit_j] indicates that position_j is the position of the j^th factory and that the j^th factory can repair at most limit_j robots.
The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.
All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.
At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.
Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that
All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.

Example 1:
Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.

Example 2:
Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.

Constraints:
1 <= robot.length, factory.length <= 100
factory[j].length == 2
-10^9 <= robot[i], positionj <= 10^9
0 <= limitj <= robot.length
The input will be generated such that it is always possible to repair every robot.

Hint 1
Sort robots and factories by their positions.

Hint 2
After sorting, notice that each factory should repair some subsegment of robots.

Hint 3
Find the minimum total distance to repair first i robots with first j factories.
"""
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
      # Sort robots and factories by their positions
      robot.sort()
      factory.sort()

      # Get number of robots and factories
      n = len(robot)
      m = len(factory)

      # Initialize dp array with large values
      dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
      dp[0][0] = 0  # No robots, no distance needed

      # Fill DP table
      for j in range(m):  # Iterate over each factory
          position_j, limit_j = factory[j]

          # Propagate previous state for each robot
          for i in range(n + 1):
              if dp[i][j] < float('inf'):  # Only if reachable
                  dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])

              # Calculate cumulative distance for assigning up to limit_j robots to factory j
              cumulative_distance = 0
              for k in range(1, limit_j + 1):
                  if i + k > n:
                      break  # Prevent going out of bounds

                  cumulative_distance += abs(robot[i + k - 1] - position_j)
                  
                  # Update dp for i + k robots with j + 1 factories
                  dp[i + k][j + 1] = min(dp[i + k][j + 1], dp[i][j] + cumulative_distance)

      # Return the minimum total distance to repair all robots with all factories
      return dp[n][m]
    
# Test cases
s = Solution()
print(s.minimumTotalDistance([0,4,6], [[2,2],[6,2]]) == 4)
print(s.minimumTotalDistance([1,-1], [[-2,1],[2,1]]) == 2)
print(s.minimumTotalDistance([9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]) == 6)