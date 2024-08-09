=begin
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
[[4,3,8],[9,5,1],[2,7,6]]
while this one is not:
[[3,8,4],[5,1,9],[7,6,2]]
In total, there is only one magic square inside the given grid.
Example 2:
Input: grid = [[8]]
Output: 0

Constraints:
    row == grid.length
    col == grid[i].length
    1 <= row, col <= 10
    0 <= grid[i][j] <= 15

=end
# @param {Integer[][]} grid
# @return {Integer}
def num_magic_squares_inside(grid)
  row = grid.length
  col = grid[0].length
  return 0 if row < 3 || col < 3
  count = 0
  (0..row-3).each do |i|
    (0..col-3).each do |j|
      count += 1 if is_magic_square(grid, i, j)
    end
  end
  count
end

def is_magic_square(grid, i, j)
  # Check if all numbers are unique
  numbers = []
  (i..i+2).each do |row|
    (j..j+2).each do |col|
      return false if grid[row][col] < 1 || grid[row][col] > 9
      return false if numbers.include?(grid[row][col])
      numbers << grid[row][col]
    end
  end
  # Check if sum of rows, columns and diagonals are equal
  sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]
  return false if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != sum
  return false if grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != sum
  return false if grid[i][j] + grid[i+1][j] + grid[i+2][j] != sum
  return false if grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != sum
  return false if grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != sum
  return false if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != sum
  return false if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != sum
  true
end

# Test cases
puts num_magic_squares_inside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]) == 1
puts num_magic_squares_inside([[8]]) == 0