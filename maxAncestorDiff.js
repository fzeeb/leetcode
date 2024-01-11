function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
 
var maxAncestorDiff = function(root) {
  let maxDiff = 0;
  const diff = (node, min, max) => {
    if (node === null) return;
    maxDiff = Math.max(maxDiff, Math.abs(node.val - min), Math.abs(node.val - max));
    min = Math.min(min, node.val);
    max = Math.max(max, node.val);
    diff(node.left, min, max);
    diff(node.right, min, max);
  };
  diff(root, root.val, root.val);
  return maxDiff;
};

const root = new TreeNode(
  8,
  new TreeNode(3, new TreeNode(1), new TreeNode(6, new TreeNode(4), new TreeNode(7))),
  new TreeNode(10, null, new TreeNode(14, new TreeNode(13), null))
);

console.log(maxAncestorDiff(root)) // 7