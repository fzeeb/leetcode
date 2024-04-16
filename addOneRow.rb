=begin
Given the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

    Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
    cur's original left subtree should be the left subtree of the new left subtree root.
    cur's original right subtree should be the right subtree of the new right subtree root.
    If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.

Constraints:

    The number of nodes in the tree is in the range [1, 10^4].
    The depth of the tree is in the range [1, 10^4].
    -100 <= Node.val <= 100
    -10^5 <= val <= 10^5
    1 <= depth <= the depth of tree + 1
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
# @param {Integer} val
# @param {Integer} depth
# @return {TreeNode}
def add_one_row(root, val, depth)
    return TreeNode.new(val, root) if depth == 1
    queue = [[root, 1]]
    while !queue.empty?
        node, current_depth = queue.shift
        if current_depth == depth - 1
            left = node.left
            right = node.right
            node.left = TreeNode.new(val, left)
            node.right = TreeNode.new(val, nil, right)
        else
            queue.push([node.left, current_depth + 1]) if node.left
            queue.push([node.right, current_depth + 1]) if node.right
        end
    end
    return root  
end

puts add_one_row(TreeNode.new(4, TreeNode.new(2, TreeNode.new(3), TreeNode.new(1)), TreeNode.new(6, TreeNode.new(5))), 1, 2) # [4,1,1,2,nil,nil,6,3,1,5]