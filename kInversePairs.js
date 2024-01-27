/*
For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 10^9 + 7.
*/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kInversePairs = function(n, k) {
    const dp = new Array(n + 1).fill(0).map(() => new Array(k + 1).fill(0));
    const mod = 1e9 + 7;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j <= k; j++) {
            if (j === 0) {
                dp[i][j] = 1;
            } else {
                for (let p = 0; p <= Math.min(j, i - 1); p++) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % mod;
                }
            }
        }
    }
    return dp[n][k];
};

const n = 3, k = 0;
console.log(kInversePairs(n, k)); // 1

/*
const n = 3, k = 1;
console.log(kInversePairs(n, k)); // 2
*/
