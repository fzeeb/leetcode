/*
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
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
 * @return {number}
 */

function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}

var pseudoPalindromicPaths  = function(root) {
  const count = new Array(10).fill(0);
  let result = 0;

  const dfs = (node) => {
    if (node === null) return;
    count[node.val]++;
    if (node.left === null && node.right === null) {
      let odd = 0;
      for (let i = 0; i < 10; i++) {
        if (count[i] % 2 === 1) odd++;
      }
      if (odd <= 1) result++;
    } else {
      dfs(node.left);
      dfs(node.right);
    }
    count[node.val]--;
  };

  dfs(root);
  return result;
};

const root = new TreeNode(
  2,
  new TreeNode(3, new TreeNode(3), new TreeNode(9)),
  new TreeNode(1, null, new TreeNode(1))
);

console.log(pseudoPalindromicPaths(root)); // 2