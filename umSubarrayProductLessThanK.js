// Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function(nums, k) {
  let count = 0;
  let product = 1;
  let left = 0;
  for (let right = 0; right < nums.length; right++) {
    product *= nums[right];
    while (product >= k && left <= right) {
      product /= nums[left];
      left++;
    }
    count += right - left + 1;
  }
  return count;
};

let nums = [10,5,2,6], k = 100
console.log(numSubarrayProductLessThanK(nums, k)) // 8