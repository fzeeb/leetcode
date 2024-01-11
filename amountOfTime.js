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
 * @param {number} start
 * @return {number}
 */

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }

var amountOfTime = function(root, start) {
  const graph = new Map();
  const queue = [[start, 0]];
  const infected = new Set();

  const buildGraph = (node, parent) => {
    if (node === null) return;
    if (!graph.has(node.val)) graph.set(node.val, new Set());
    if (parent !== null) {
      graph.get(node.val).add(parent.val);
      graph.get(parent.val).add(node.val);
    }
    buildGraph(node.left, node);
    buildGraph(node.right, node);
  };

  buildGraph(root, null);

  let minutes = 0;
  while (queue.length > 0) {
    const [node, time] = queue.pop();
    if (!infected.has(node)) {
      infected.add(node);
      minutes = Math.max(minutes, time);
      for (const neighbor of graph.get(node)) {
        if (!infected.has(neighbor)) {
          queue.unshift([neighbor, time + 1]);
        }
      }
    }
  }

  return minutes;
};

const root = new TreeNode(
  1,
  new TreeNode(5, null, new TreeNode(4, new TreeNode(9), new TreeNode(2))),
  new TreeNode(3, new TreeNode(10), new TreeNode(6))
);
const start = 3;
console.log(amountOfTime(root, start)); // Output: 4