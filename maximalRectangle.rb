=begin
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Constraints:

    rows == matrix.length
    cols == matrix[i].length
    1 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.
=end
def maximal_rectangle(matrix)
  maxArea = 0
  rows = matrix.length
  cols = matrix[0].length
  heights = Array.new(cols) {0}
  for i in 0...rows
    for j in 0...cols
      heights[j] = matrix[i][j] == '1' ? heights[j] + 1 : 0
    end
    maxArea = [maxArea, largestRectangleArea(heights)].max
  end
  maxArea
end

def largestRectangleArea(heights)
  stack = []
  maxArea = 0
  heights.push(0)
  for i in 0...heights.length
    while !stack.empty? && heights[i] < heights[stack[-1]]
      h = heights[stack.pop]
      w = stack.empty? ? i : i - stack[-1] - 1
      maxArea = [maxArea, h * w].max
    end
    stack.push(i)
  end
  maxArea
end

puts maximal_rectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) # 6