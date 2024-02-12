/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let map = new Map();
  for (let i = 0; i < nums.length; i++) {
      if (map.has(nums[i])) {
          map.set(nums[i], map.get(nums[i]) + 1);
      } else {
          map.set(nums[i], 1);
      }
  }
  for (let [key, value] of map) {
      if (value > nums.length / 2) {
          return key;
      }
  }

  return -1;
}
const nums = [3,2,3];
console.log(majorityElement(nums)); // 3