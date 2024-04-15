=begin
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -1000 <= Node.val <= 1000
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
# @return {Integer}
def sum_of_left_leaves(root)
  return 0 if root.nil?
  return root.left.val + sum_of_left_leaves(root.right) if root.left && root.left.left.nil? && root.left.right.nil?
  sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right) 
end

puts sum_of_left_leaves(TreeNode.new(3, TreeNode.new(9), TreeNode.new(20, TreeNode.new(15), TreeNode.new(7)))) # 24