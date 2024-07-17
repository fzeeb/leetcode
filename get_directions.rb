=begin
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.
Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:
    'L' means to go from a node to its left child node.
    'R' means to go from a node to its right child node.
    'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.

Constraints:
    The number of nodes in the tree is n.
    2 <= n <= 105
    1 <= Node.val <= n
    All the values in the tree are unique.
    1 <= startValue, destValue <= n
    startValue != destValue

Hint 1
The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). The path will travel upwards from node s to the LCA and then downwards from the LCA to node t.

Hint 2
Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?

Hint 3
Remove the longest common prefix of the two path strings to get the path LCA → s, and LCA → t. Each step in the path of LCA → s should be reversed as 'U'.
=end
# Definition for a binary tree node.
class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end
# @param {TreeNode} root
# @param {Integer} start_value
# @param {Integer} dest_value
# @return {String}
def get_directions(root, start_value, dest_value)
  def dfs(node, target, path)
    return false if node.nil?
    return true if node.val == target
    
    path << 'L'
    return true if dfs(node.left, target, path)
    path.pop()
    
    path << 'R'
    return true if dfs(node.right, target, path)
    path.pop()
    
    false
  end

  start_path = []
  dest_path = []
  dfs(root, start_value, start_path)
  dfs(root, dest_value, dest_path)
  start_path = start_path.join('')
  dest_path = dest_path.join('')
  
  lcp = 0
  while lcp < start_path.length && lcp < dest_path.length && start_path[lcp] == dest_path[lcp]
    lcp += 1
  end
  
  'U' * (start_path.length - lcp) + dest_path[lcp..-1]
end

# root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
root = TreeNode.new(5)
root.left = TreeNode.new(1)
root.right = TreeNode.new(2)
root.left.left = TreeNode.new(3)
root.right.left = TreeNode.new(6)
root.right.right = TreeNode.new(4)
p get_directions(root, 3, 6) # "UURL"
