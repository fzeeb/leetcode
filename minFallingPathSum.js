/*
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
*/

/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {
  let min = Infinity;
  const n = matrix.length;
  const dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    dp[0][i] = matrix[0][i];
  }
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < n; j++) {
      let left = dp[i - 1][j - 1] === undefined ? Infinity : dp[i - 1][j - 1];
      let right = dp[i - 1][j + 1] === undefined ? Infinity : dp[i - 1][j + 1];
      dp[i][j] = Math.min(left, right, dp[i - 1][j]) + matrix[i][j];
    }
  }
  for (let i = 0; i < n; i++) {
    min = Math.min(min, dp[n - 1][i]);
  }
  return min;
};

const matrix = [[2,1,3],[6,5,4],[7,8,9]];
console.log(minFallingPathSum(matrix)); // 13