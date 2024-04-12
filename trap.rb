=begin
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Constraints:

    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
=end
# @param {Integer[]} height
# @return {Integer}
def trap(height)
    left = 0
    right = height.length - 1
    leftMax = 0
    rightMax = 0
    result = 0

    while left < right
      if height[left] < height[right]
        if height[left] >= leftMax
          leftMax = height[left]
        else
          result += leftMax - height[left]
        end
        left += 1
      else
        if height[right] >= rightMax
          rightMax = height[right]
        else
          result += rightMax - height[right]
        end
        right -= 1
      end
    end

    return result
  end

  # Test cases
  puts trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
  puts trap([4,2,0,3,2,5]) # 9

# Test cases
puts trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
puts trap([4,2,0,3,2,5]) # 9