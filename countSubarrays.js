/*
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
*/
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
  let count = 0;
  let max_num = Math.max(...nums);
  let windowStart = 0;
  let maxCount = 0;

  for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
    if (nums[windowEnd] === max_num) {
      maxCount++;
    }

    while (maxCount >= k) {
      count += nums.length - windowEnd;
      if (nums[windowStart] === max_num) {
        maxCount--;
      }
      windowStart++;
    }
  }

  return count;
};

/*
Example 1:
nums = [1,3,2,3,3], k=2, Expected output: 6
Example 2:
nums = [1,4,2,1], k=3, Expected output: 0
Example 3:
nums = [28,5,58,91,24,91,53,9,48,85,16,70,91,91,47,91,61,4,54,61,49], k=1, Expected output: 187
*/