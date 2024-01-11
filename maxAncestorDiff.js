function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
 
var maxAncestorDiff = function(root) {
    
};

root = [8,3,10,1,6,null,14,null,null,4,7,13]
const root = new TreeNode(
  8,
  new TreeNode(3, new TreeNode(1), new TreeNode(6, new TreeNode(4), new TreeNode(7))),
  new TreeNode(10, null, new TreeNode(14, new TreeNode(13), null))
);

console.log(maxAncestorDiff(root)) // 7