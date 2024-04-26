/*
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

  t is a subsequence of the string s.
  The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.

Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.

 

Constraints:

    1 <= s.length <= 10^5
    0 <= k <= 25
    s consists of lowercase English letters.
*/
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestIdealString = function(s, k) {
  var dp = new Array(26).fill(0);
  
  for (var i = 0; i < s.length; i++) {
    var char = s[i];
    var idx = char.charCodeAt(0) - 'a'.charCodeAt(0);
    var max_length = dp[idx] + 1;
    
    for (var j = Math.max(-k, -idx); j <= Math.min(k, 26 - idx - 1); j++) {
      if (0 <= idx + j && idx + j < 26) {
        max_length = Math.max(max_length, dp[idx + j] + 1);
      }
    }
    
    dp[idx] = Math.max(dp[idx], max_length);
  }
  
  return Math.max(...dp);
};

console.log(longestIdealString("acfgbd", 2)); // 4
console.log(longestIdealString("abcd", 3)); // 4
console.log(longestIdealString("jxhwaysa", 14)); // 5