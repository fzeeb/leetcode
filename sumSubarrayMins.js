/*
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo e.g. 10^9 + 7.
*/
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumSubarrayMins = function(arr) {
  let sum = 0;
  const MOD = 1000000007;
  const stack = [];
  arr = [0, ...arr, 0];
  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[i] < arr[stack[stack.length - 1]]) {
      const j = stack.pop();
      const k = stack[stack.length - 1];
      sum += arr[j] * (i - j) * (j - k);
      sum %= MOD;
    }
    stack.push(i);
  }
  return sum; 
};

const arr = [3,1,2,4]
console.log(sumSubarrayMins(arr)); // 17