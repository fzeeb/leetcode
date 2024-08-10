=begin
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
Given the grid grid represented as a string array, return the number of regions.
Note that backslash characters are escaped, so a '\' is represented as '\\'.

Example 1:
Input: grid = [" /","/ "]
Output: 2

Example 2:
Input: grid = [" /","  "]
Output: 1

Example 3:
Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 30
    grid[i][j] is either '/', '\', or ' '.
=end
# @param {String[]} grid
# @return {Integer}
def regions_by_slashes(grid)
  n = grid.length
  graph = Array.new(n * 3) { Array.new(n * 3, 0) }
  for i in 0...n
    for j in 0...n
      if grid[i][j] == '/'
        graph[i * 3][j * 3 + 2] = 1
        graph[i * 3 + 1][j * 3 + 1] = 1
        graph[i * 3 + 2][j * 3] = 1
      elsif grid[i][j] == '\\'
        graph[i * 3][j * 3] = 1
        graph[i * 3 + 1][j * 3 + 1] = 1
        graph[i * 3 + 2][j * 3 + 2] = 1
      end
    end
  end
  regions = 0
  for i in 0...(n * 3)
    for j in 0...(n * 3)
      if graph[i][j] == 0
        dfs(graph, i, j)
        regions += 1
      end
    end
  end
  regions 
end

def dfs(graph, i, j)
  if i >= 0 && i < graph.length && j >= 0 && j < graph[0].length && graph[i][j] == 0
    graph[i][j] = 1
    dfs(graph, i - 1, j)
    dfs(graph, i + 1, j)
    dfs(graph, i, j - 1)
    dfs(graph, i, j + 1)
  end
end

# Test  cases
puts regions_by_slashes([" /","/ "]) == 2
puts regions_by_slashes([" /","  "]) == 1
puts regions_by_slashes(["/\\","\\/"]) == 5