=begin
A binary tree is named Even-Odd if it meets the following conditions:

The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
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
# @param {TreeNode} root
# @return {Boolean}
def is_even_odd_tree(root)
  queue = [root]
  level = 0
  while !queue.empty?
    size = queue.size
    prev = level.even? ? 0 : 10**6
    size.times do
      node = queue.shift
      if level.even?
        return false if node.val.even? || node.val <= prev
      else
        return false if node.val.odd? || node.val >= prev
      end
      prev = node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    level += 1
  end
  true
end