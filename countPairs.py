"""
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Constraints:
    The number of nodes in the tree is in the range [1, 210].
    1 <= Node.val <= 100
    1 <= distance <= 10

Hint 1
Start DFS from each leaf node. stop the DFS when the number of steps done > distance.

Hint 2
If you reach another leaf node within distance steps, add 1 to the answer.

int 3
Note that all pairs will be counted twice so divide the answer by 2.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        solution = 0

        def dfs(node):
            nonlocal solution
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for l in left:
                for r in right:
                    if l + r <= distance:
                        solution += 1
            return [i + 1 for i in left + right if i + 1 < distance]
        
        dfs(root)
        return solution
    
# Main Call
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

distance = 3
solution = Solution()
print(solution.countPairs(root, distance))
