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
  let count = 0;
  const dfs = (node, path) => {
    if (node === null) return;
    path.push(node.val);
    if (node.left === null && node.right === null) {
      if (isPalindrome(path)) count++;
      path.pop();
      return;
    }
    dfs(node.left, path);
    dfs(node.right, path);
    path.pop();
  };
  dfs(root, []);
  return count;
};

function isPalindrome(arr) {
  const map = new Map();
  for (const num of arr) {
    if (!map.has(num)) map.set(num, 0);
    map.set(num, map.get(num) + 1);
  }
  let oddCount = 0;
  for (const [key, val] of map) {
    if (val % 2 === 1) oddCount++;
  }
  return oddCount <= 1;
}

const root = new TreeNode(
  2,
  new TreeNode(3, new TreeNode(3), new TreeNode(9)),
  new TreeNode(1, null, new TreeNode(1))
);

console.log(pseudoPalindromicPaths(root)); // 2