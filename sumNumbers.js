/*
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

    For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    0 <= Node.val <= 9
    The depth of the tree will not exceed 10.
*/
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}
/**
 * @param {TreeNode} root
 * @return {number}
 */
var sumNumbers = function(root) {
    let sum = 0;
    const traverse = (node, path) => {
        if (!node) return;
        path += node.val;
        if (!node.left && !node.right) {
            sum += parseInt(path);
        }
        traverse(node.left, path);
        traverse(node.right, path);
    };
    traverse(root, '');
    return sum;
};

console.log(sumNumbers(new TreeNode(1, new TreeNode(2), new TreeNode(3)))); // 25