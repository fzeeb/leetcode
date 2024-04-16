from typing import Optional
"""
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
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        self.dfs(root, val, depth, 1)
        return root
    
    def dfs(self, node, val, depth, current_depth):
        if not node:
            return
        if current_depth == depth - 1:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)
            return
        self.dfs(node.left, val, depth, current_depth + 1)
        self.dfs(node.right, val, depth, current_depth + 1)

root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, TreeNode(5)))
result = Solution().addOneRow(root, 1, 2)
print(result.val)  # 4
print(result.left.val)  # 1
print(result.right.val)  # 1
print(result.left.left.val)  # 2
print(result.left.right)  # None
print(result.right.left)  # None
print(result.right.right.val)  # 6
print(result.left.left.left.val)  # 3
print(result.left.left.right.val)  # 1
print(result.right.right.left.val)  # 5