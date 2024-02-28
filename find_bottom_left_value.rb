# Given the root of a binary tree, return the leftmost value in the last row of the tree.
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
# @return {Integer}
def find_bottom_left_value(root)
  queue = [root]
  while !queue.empty?
    root = queue.shift
    queue << root.right if root.right
    queue << root.left if root.left
  end
  root.val
end

