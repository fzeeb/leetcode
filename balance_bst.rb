=begin
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:
Input: root = [2,1,3]
Output: [2,1,3]

Constraints:
    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

Hint 1
Convert the tree to a sorted array using an in-order traversal.

Hint 2
Construct a new balanced tree from the sorted array recursively.
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
# @return {TreeNode}
def balance_bst(root)
  inorder = []
  def traverse(node, inorder)
    if node.nil?
      return
    end
    traverse(node.left, inorder)
    inorder << node.val
    traverse(node.right, inorder)
  end
  traverse(root, inorder)
  def build_tree(inorder)
    if inorder.empty?
      return nil
    end
    mid = inorder.size / 2
    node = TreeNode.new(inorder[mid])
    node.left = build_tree(inorder[0...mid])
    node.right = build_tree(inorder[mid+1..-1])
    node
  end
  build_tree(inorder)
end

# Helper function to print tree level order, not needed for the solution
def print_tree_level_order(root)
  return [] if root.nil?
  queue = [root]
  result = []
  while !queue.empty?
    current_level_size = queue.size
    current_level = []
    current_level_size.times do
      node = queue.shift
      if node.nil?
        current_level << nil
      else
        current_level << node.val
        queue.push(node.left, node.right)
      end
    end
    result << current_level
  end
  result
end

root = TreeNode.new(1, nil, TreeNode.new(2, nil, TreeNode.new(3, nil, TreeNode.new(4))))
print print_tree_level_order(balance_bst(root)) # [[3], [2, 4], [1]]