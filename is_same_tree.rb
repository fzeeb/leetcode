=begin
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
E.g.
Input: p = [1,2,3], q = [1,2,3] Output: true
Input: p = [1,2], q = [1,null,2] Output: false
Input: p = [1,2,1], q = [1,1,2] Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
-10^4 <= Node.val <= 10^4
=end
# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} p
# @param {TreeNode} q
# @return {Boolean}
def is_same_tree(p, q)
  return true if p.nil? && q.nil?
  return false if p.nil? || q.nil?
  return false if p.val != q.val
  is_same_tree(p.left, q.left) && is_same_tree(p.right, q.right)
end