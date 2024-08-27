=begin
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

 
Constraints:
    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes.

Hint 1
Multiplying probabilities will result in precision errors.

Hint 2
Take log probabilities to sum up numbers instead of multiplying them.

Hint 3
Use Dijkstra's algorithm to find the minimum path between the two nodes after negating all costs.
=end
# @param {Integer} n
# @param {Integer[][]} edges
# @param {Float[]} succ_prob
# @param {Integer} start_node
# @param {Integer} end_node
# @return {Float}
def max_probability(n, edges, succ_prob, start_node, end_node)
  graph = Hash.new { |h, k| h[k] = [] }
  edges.each_with_index do |edge, i|
    graph[edge[0]] << [edge[1], succ_prob[i]]
    graph[edge[1]] << [edge[0], succ_prob[i]]
  end
  dist = Array.new(n, 0)
  dist[start_node] = 1
  pq = [[-1, start_node]]
  while !pq.empty?
    prob, node = pq.shift
    prob = -prob
    next if prob < dist[node]
    graph[node].each do |neighbour|
      neighbour_node, neighbour_prob = neighbour
      if dist[neighbour_node] < dist[node] * neighbour_prob
        dist[neighbour_node] = dist[node] * neighbour_prob
        pq << [-dist[neighbour_node], neighbour_node]
      end
    end
  end
  dist[end_node]
end

# Test cases
puts max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2) == 0.25000
puts max_probability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2) == 0.30000