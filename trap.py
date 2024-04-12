from typing import List

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:

  n == height.length
  1 <= n <= 2 * 104
  0 <= height[i] <= 105
"""
class Solution:
    def trap(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      leftMax = 0
      rightMax = 0
      result = 0

      while left < right:
        if height[left] < height[right]:
          if height[left] >= leftMax:
            leftMax = height[left]
          else:
            result += leftMax - height[left]
          left += 1
        else:
          if height[right] >= rightMax:
            rightMax = height[right]
          else:
            result += rightMax - height[right]
          right -= 1

      return result

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(Solution().trap([4,2,0,3,2,5])) # 9