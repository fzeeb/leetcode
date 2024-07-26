=begin
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [from_i, to_i, weight_i] represents a bidirectional and weighted edge between cities from_i and to_i, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Example 1:
Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:
Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

Constraints:
    2 <= n <= 100
    1 <= edges.length <= n * (n - 1) / 2
    edges[i].length == 3
    0 <= from_i < to_i < n
    1 <= weight_i, distanceThreshold <= 10^4
    All pairs (from_i, to_i) are distinct.

Hint 1
Use Floyd-Warshall's algorithm to compute any-point to any-point distances. (Or can also do Dijkstra from every node due to the weights are non-negative).

Hint 2
For each city calculate the number of reachable cities within the threshold, then search for the optimal city.
=end
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} distance_threshold
# @return {Integer}
def find_the_city(n, edges, distance_threshold)
  dist = Array.new(n) { Array.new(n, Float::INFINITY) }
  for i in 0..n-1
    dist[i][i] = 0
  end
  for edge in edges
    from_i, to_i, weight_i = edge
    dist[from_i][to_i] = weight_i
    dist[to_i][from_i] = weight_i
  end
  for k in 0..n-1
    for i in 0..n-1
      for j in 0..n-1
        dist[i][j] = [dist[i][j], dist[i][k] + dist[k][j]].min
      end
    end
  end
  min_reachable = n
  min_city = 0
  for i in 0..n-1
    reachable = 0
    for j in 0..n-1
      if i != j && dist[i][j] <= distance_threshold
        reachable += 1
      end
    end
    if reachable <= min_reachable
      min_reachable = reachable
      min_city = i
    end
  end
  min_city   
end

# Test cases
puts find_the_city(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4) # 3
puts find_the_city(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2) # 0