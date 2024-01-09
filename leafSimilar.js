/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {
  // create two arrays
  const leaf1 = [];
  const leaf2 = [];

  // create helper function that takes in a node and an array
  const helper = (node, arr) => {
    // if node is null, return
    if (!node) return;
    // if node is a leaf, push to array
    if (!node.left && !node.right) arr.push(node.val);
    // call helper on left
    helper(node.left, arr);
    // call helper on right
    helper(node.right, arr);
  };

  // call helper on root1
  helper(root1, leaf1);

  // call helper on root2
  helper(root2, leaf2);

  // return true if arrays are equal
  return leaf1.toString() === leaf2.toString();
};

let root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8];
console.log(leafSimilar(root1, root2)); // true