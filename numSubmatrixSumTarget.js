/*
Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
*/
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {number}
 */
var numSubmatrixSumTarget = function(matrix, target) {
  let count = 0;
  for (let i = 0; i < matrix.length; i++) {
    let rowSum = new Array(matrix[0].length).fill(0);
    for (let j = i; j < matrix.length; j++) {
      for (let k = 0; k < matrix[0].length; k++) {
        rowSum[k] += matrix[j][k];
      }
      count += subArraySum(rowSum, target);
    }
  }
  return count;
};


function subArraySum(arr, target) {
  let count = 0;
  let sum = 0;
  let map = new Map();
  map.set(0, 1);
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
    if (map.has(sum - target)) {
      count += map.get(sum - target);
    }
    map.set(sum, (map.get(sum) || 0) + 1);
  }
  return count;
}

const matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0;
console.log(numSubmatrixSumTarget(matrix, target)); // 4