/*
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarrayLength = function(nums, k) {
  let freq = {};
  let left = 0;
  let maxLen = 0;

  for (let right = 0; right < nums.length; right++) {
      if (!freq[nums[right]]) {
          freq[nums[right]] = 0;
      }
      freq[nums[right]]++;

      while (freq[nums[right]] > k) {
          freq[nums[left]]--;
          left++;
      }

      maxLen = Math.max(maxLen, right - left + 1);
  }

  return maxLen;
};

let nums = [1,2,3,1,2,3,1,2], k = 2
console.log(maxSubarrayLength(nums, k)) // 6