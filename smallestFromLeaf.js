/*
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

    For example, "ab" is lexicographically smaller than "aba".

A leaf of a node is a node that has no children.

Constraints:

    The number of nodes in the tree is in the range [1, 8500].
    0 <= Node.val <= 25
*/
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string}
 */
var smallestFromLeaf = function(root) {
    let result = '';
    const dfs = (node, path) => {
        if (!node) return;
        path = String.fromCharCode(node.val + 97) + path;
        if (!node.left && !node.right) {
            if (!result) result = path;
            else result = path < result ? path : result;
        }
        dfs(node.left, path);
        dfs(node.right, path);
    };
    dfs(root, '');
    return result;
};