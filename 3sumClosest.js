/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
  // sort the array
  nums.sort((a, b) => a - b);

  // set the closest variable
  let closest = Infinity;

  // loop through the array
  for (let i = 0; i < nums.length - 2; i++) {
    // set the left and right pointers
    let left = i + 1;
    let right = nums.length - 1;

    // loop while left is less than right
    while (left < right) {
      // get the sum of the three elements
      let sum = nums[i] + nums[left] + nums[right];

      // check if the sum is equal to the target
      if (sum === target) {
        // return the sum
        return sum;
      } else if (sum < target) {
        // check if the difference between the target and sum is less than the difference between the target and closest
        if (Math.abs(target - sum) < Math.abs(target - closest)) {
          // set the closest to the sum
          closest = sum;
        }

        // increment the left pointer
        left++;
      } else {
        // check if the difference between the target and sum is less than the difference between the target and closest
        if (Math.abs(target - sum) < Math.abs(target - closest)) {
          // set the closest to the sum
          closest = sum;
        }

        // decrement the right pointer
        right--;
      }
    }
  }

  // return the closest
  return closest;
};

module.exports = threeSumClosest;