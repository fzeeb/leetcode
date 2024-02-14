/*
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
  for (let i = 0; i < nums.length; i++) {
    if (i % 2 === 0 && nums[i] < 0) {
      for (let j = i + 1; j < nums.length; j++) {
        if (nums[j] > 0) {
          let temp = nums[i];
          nums[i] = nums[j];
          nums[j] = temp;
          break;
        }
      }
    } else if (i % 2 !== 0 && nums[i] > 0) {
      for (let j = i + 1; j < nums.length; j++) {
        if (nums[j] < 0) {
          let temp = nums[i];
          nums[i] = nums[j];
          nums[j] = temp;
          break;
        }
      }
    }
  }
  return nums;
};

const nums = [3,1,-2,-5,2,-4];
console.log(rearrangeArray(nums)); // [3,-2,1,-5,2,-4]