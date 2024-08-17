=begin
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c_1) and (r + 1, c_2) will subtract abs(c_1 - c_2) from your score.
Return the maximum number of points you can achieve.
abs(x) is defined as:
    x for x >= 0.
    -x for x < 0.

Example 1:
Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.

Example 2:
Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.

Constraints:
    m == points.length
    n == points[r].length
    1 <= m, n <= 10^  5
    1 <= m * n <= 10^5
    0 <= points[r][c] <= 10^5

Hint 1
Try using dynamic programming.

Hint 2
dp[i][j] is the maximum number of points you can have if points[i][j] is the most recent cell you picked.
=end
# @param {Integer[][]} points
# @return {Integer}
def max_points(points)
  m = points.length
  n = points[0].length
  dp = points[0].dup

  (1...m).each do |i|
    left_dp = Array.new(n, 0)
    right_dp = Array.new(n, 0)

    # Left-to-right pass
    left_dp[0] = dp[0]
    (1...n).each do |j|
      left_dp[j] = [left_dp[j-1] - 1, dp[j]].max
    end

    # Right-to-left pass
    right_dp[n-1] = dp[n-1]
    (n-2).downto(0) do |j|
      right_dp[j] = [right_dp[j+1] - 1, dp[j]].max
    end

    # Calculate new dp for the current row
    new_dp = Array.new(n, 0)
    (0...n).each do |j|
      new_dp[j] = points[i][j] + [left_dp[j], right_dp[j]].max
    end

    dp = new_dp
  end

  dp.max
end

 # Test cases
  puts max_points([[1,2,3],[1,5,1],[3,1,1]]) == 9
  puts max_points([[1,5],[2,3],[4,2]]) == 11