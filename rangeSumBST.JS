//Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

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
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function(root, low, high) {
  // create a sum variable
  let sum = 0;
  // create a helper function that takes in a node
  const helper = (node) => {
    // if node is null, return
    if (!node) return;
    // if node value is greater than or equal to low and less than or equal to high, add to sum
    if (node.val >= low && node.val <= high) sum += node.val;
    // call helper on left
    helper(node.left);
    // call helper on right
    helper(node.right);
  };
  // call helper on root
  helper(root);
  // return sum
  return sum;
};

const root = [10,5,15,3,7,null,18], low = 7, high = 15;
console.log(rangeSumBST(root, low, high)); // 32