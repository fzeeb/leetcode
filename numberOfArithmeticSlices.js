// Given an integer array nums, return the number of all the arithmetic subsequences of nums.
/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfArithmeticSlices = function(nums) {
  let count = 0;
  let placeholder = Array(nums.length).fill(0).map(() => new Map());
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      let diff = nums[i] - nums[j];
      let prev = placeholder[j].get(diff) || 0;
      count += prev;
      placeholder[i].set(diff, (placeholder[i].get(diff) || 0) + prev + 1);
    }
  }
  return count;
};

let nums = [2,4,6,8,10]
console.log(numberOfArithmeticSlices(nums)) // 7