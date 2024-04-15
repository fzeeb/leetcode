=begin
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
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
def sum_numbers(root)
    return 0 if root.nil?
    return dfs(root, 0)
end

def dfs(node, sum)
    return 0 if node.nil?
    sum = sum * 10 + node.val
    return sum if node.left.nil? && node.right.nil?
    return dfs(node.left, sum) + dfs(node.right, sum)
end

puts sum_numbers(TreeNode.new(1, TreeNode.new(2), TreeNode.new(3))) # 25