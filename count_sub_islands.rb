=begin
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
Return the number of islands in grid2 that are considered sub-islands.

Example 1:
Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

Example 2:
Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

Constraints:
    m == grid1.length == grid2.length
    n == grid1[i].length == grid2[i].length
    1 <= m, n <= 500
    grid1[i][j] and grid2[i][j] are either 0 or 1.

int 1
Let's use floodfill to iterate over the islands of the second grid

Hint 2
Let's note that if all the cells in an island in the second grid if they are represented by land in the first grid then they are connected hence making that island a sub-island
=end
# @param {Integer[][]} grid1
# @param {Integer[][]} grid2
# @return {Integer}
def count_sub_islands(grid1, grid2)
    m, n = grid1.size, grid1[0].size
    sub_islands = 0
    visited = Array.new(m) { Array.new(n, false) }
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    (0...m).each do |i|
        (0...n).each do |j|
        next if visited[i][j] || grid2[i][j] == 0
        queue = [[i, j]]
        visited[i][j] = true
        is_sub_island = true
        while !queue.empty?
            x, y = queue.shift
            is_sub_island = false if grid1[x][y] == 0
            directions.each do |dx, dy|
            nx, ny = x + dx, y + dy
            next if nx < 0 || nx >= m || ny < 0 || ny >= n || visited[nx][ny] || grid2[nx][ny] == 0
            queue << [nx, ny]
            visited[nx][ny] = true
            end
        end
        sub_islands += 1 if is_sub_island
        end
    end
    sub_islands
end

# Test cases
puts count_sub_islands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]) == 3

puts count_sub_islands([[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]) == 2
