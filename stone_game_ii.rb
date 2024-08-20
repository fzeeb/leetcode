=begin
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104

Constraints:
    1 <= piles.length <= 100
    1 <= piles[i] <= 104

Hint 1
Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.
=end
# @param {Integer[]} piles
# @return {Integer}
# @param {Integer[]} piles
# @return {Integer}
# @param {Integer[]} piles
# @return {Integer}
def stone_game_ii(piles)
  n = piles.length
  suffix_sum = Array.new(n + 1, 0)
  dp = Array.new(n) { Array.new(n + 1, 0) }

  # Calculate suffix sum
  (n - 1).downto(0) do |i|
    suffix_sum[i] = suffix_sum[i + 1] + piles[i]
  end

  # Fill dp table
  (n - 1).downto(0) do |i|
    (1..n).each do |m|
      if i + 2 * m >= n
        dp[i][m] = suffix_sum[i]
      else
        dp[i][m] = suffix_sum[i] - (1..2*m).map { |x| dp[i + x][[ m, x ].max] }.min
      end
    end
  end

  dp[0][1]
end


# Test cases
puts stone_game_ii([2,7,9,4,4]) == 10
puts stone_game_ii([1,2,3,4,5,100]) == 104