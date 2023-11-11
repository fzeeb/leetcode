/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
  // sort the array
  nums.sort((a, b) => a - b);

  // create a result array
  let result = [];

  // loop through the array
  for (let i = 0; i < nums.length - 2; i++) {
    // check if the current element is the same as the previous element
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    // set the left and right pointers
    let left = i + 1;
    let right = nums.length - 1;

    // loop while left is less than right
    while (left < right) {
      // get the sum of the three elements
      let sum = nums[i] + nums[left] + nums[right];

      // check if the sum is 0
      if (sum === 0) {
        // push the elements into the result array
        result.push([nums[i], nums[left], nums[right]]);

        // increment the left pointer
        left++;

        // decrement the right pointer
        right--;

        // check if the left element is the same as the previous element
        while (left < right && nums[left] === nums[left - 1]) {
          left++;
        }

        // check if the right element is the same as the previous element
        while (left < right && nums[right] === nums[right + 1]) {
          right--;
        }
      } else if (sum < 0) {
        // increment the left pointer
        left++;
      } else {
        // decrement the right pointer
        right--;
      }
    }
  }

  // return the result array
  return result;
};

// export the function
module.exports = threeSum;