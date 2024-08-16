=begin
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.

Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array

Example 2:
Input: arrays = [[1],[1]]
Output: 0

Constraints:
    m == arrays.length
    2 <= m <= 10^5
    1 <= arrays[i].length <= 500
    -10^4 <= arrays[i][j] <= 10^4
    arrays[i] is sorted in ascending order.
    There will be at most 10^5 integers in all the arrays.
=end
# @param {Integer[][]} arrays
# @return {Integer}
def max_distance(arrays)
  min = arrays[0][0]
  max = arrays[0][-1]
  max_distance = 0
  (1...arrays.length).each do |i|
    max_distance = [max_distance, (arrays[i][0] - max).abs, (arrays[i][-1] - min).abs].max
    min = [min, arrays[i][0]].min
    max = [max, arrays[i][-1]].max
  end
  max_distance
end

# Test cases
puts max_distance([[1,2,3],[4,5],[1,2,3]]) == 4
puts max_distance([[1],[1]]) == 0
puts max_distance([[1,4],[0,5]]) == 4