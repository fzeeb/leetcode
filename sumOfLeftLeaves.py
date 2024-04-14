from typing import Optional
"""
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    if root.left and not root.left.left and not root.left.right:
      return root.left.val + self.sumOfLeftLeaves(root.right)
    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
print(Solution().sumOfLeftLeaves(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))))) # 24
