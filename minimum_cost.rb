=begin
ou are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].
You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
 

Example 1:
Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.

Example 2:
Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.

Example 3:
Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.

Constraints:
    1 <= source.length == target.length <= 10^5
    source, target consist of lowercase English letters.
    1 <= cost.length == original.length == changed.length <= 2000
    original[i], changed[i] are lowercase English letters.
    1 <= cost[i] <= 10^6
    original[i] != changed[i]

Hint 1
Construct a graph with each letter as a node, and construct an edge (a, b) with weight c if we can change from character a to letter b with cost c. (Keep the one with the smallest cost in case there are multiple edges between a and b).

Hint 2
Calculate the shortest path for each pair of characters (source[i], target[i]). The sum of cost over all i in the range [0, source.length - 1]. If there is no path between source[i] and target[i], the answer is -1.

Hint 3
Any shortest path algorithms will work since we only have 26 nodes. Since we only have at most 26 * 26 pairs, we can save the result to avoid re-calculation.

Hint 4
We can also use Floyd Warshall's algorithm to precompute all the results.
=end
# @param {String} source
# @param {String} target
# @param {Character[]} original
# @param {Character[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
  # Initialize the distance matrix with infinity
  inf = Float::INFINITY
  dist = Array.new(26) { Array.new(26, inf) }
  
  # Set the distance from each character to itself as 0
  26.times { |i| dist[i][i] = 0 }
  
  # Build the initial graph based on the given transformations
  original.zip(changed, cost).each do |orig, chng, cst|
    i, j = orig.ord - 'a'.ord, chng.ord - 'a'.ord
    dist[i][j] = [dist[i][j], cst].min
  end
  
  # Floyd-Warshall algorithm
  26.times do |k|
    26.times do |i|
      26.times do |j|
        if dist[i][k] + dist[k][j] < dist[i][j]
          dist[i][j] = dist[i][k] + dist[k][j]
        end
      end
    end
  end
  
  # Calculate the total cost
  total_cost = 0
  source.chars.zip(target.chars).each do |s, t|
    i, j = s.ord - 'a'.ord, t.ord - 'a'.ord
    return -1 if dist[i][j] == inf
    total_cost += dist[i][j]
  end
  
  total_cost
end

# Test cases
puts minimum_cost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]) == 28
puts minimum_cost("aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]) == 12
puts minimum_cost("abcd", "abce", ["a"], ["e"], [10000]) == -1