/*
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo e.g. 10^9 + 7.
*/
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function(arr) {
  let sum = 0;
  const n = arr.length;
  const dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
  const MOD = 1000000007; // Modulo value
  for (let i = 0; i < n; i++) {
    dp[0][i] = arr[i];
    sum += arr[i];
  }
  for (let i = 1; i < n; i++) {
    for (let j = 0; j < n - i; j++) {
      dp[i][j] = Math.min(dp[i - 1][j], dp[i - 1][j + 1]);
      sum += dp[i][j];
      sum %= MOD; // Apply modulo
    }
  }
  return sum;  
};

const arr = [3,1,2,4]
console.log(sumSubarrayMins(arr)); // 17