"""
Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Return the root of the modified tree.
Note that the depth of a node is the number of edges in the path from the root node to it.

Example 1:
Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:

Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 
Constraints:
The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 10^4

Hint 1
Use DFS two times.

Hint 2
For the first time, find the sum of values of all the levels of the binary tree.

Hint 3
For the second time, update the value of the node with the sum of the values of the current level - sibling node’s values.
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'[{self.val}, {self.left}, {self.right}]'

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = {}
        
        # First DFS to find the sum of values for each level
        def dfs(node, level):
            if not node:
                return
            if level not in levels:
                levels[level] = 0
            levels[level] += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        # Second DFS to replace the value of each node with the sum of all its cousins' values
        def replace(node, level):
            if not node:
                return
            if node.left and node.right:
                sibling_sum = node.left.val + node.right.val
                if level in levels:
                    node.left.val = levels[level + 1] - sibling_sum
                    node.right.val = levels[level + 1] - sibling_sum
            elif node.left:  # Only left child exists
                sibling_sum = node.left.val
                if level in levels:
                    node.left.val = levels[level + 1] - sibling_sum
            elif node.right:  # Only right child exists
                sibling_sum = node.right.val
                if level in levels:
                    node.right.val = levels[level + 1] - sibling_sum

            replace(node.left, level + 1)
            replace(node.right, level + 1)

        # First, calculate the sum of each level
        dfs(root, 0)

        # Special case: Root node does not have cousins
        if root:
            root.val = 0

        # Second, replace node values with the sum of their cousins' values
        replace(root, 0)

        return root

# Test Cases
s = Solution()
print(s.replaceValueInTree(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, TreeNode(7))))) # [0,0,0,7,7,None,11]
print(s.replaceValueInTree(TreeNode(3, TreeNode(1), TreeNode(2)))) # [0,0,0]
