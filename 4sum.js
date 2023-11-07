/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
  // check if the nums length is less than 4
  if (nums.length < 4) {
    // return an empty array
    return [];
  }

  // sort the nums array
  nums.sort((a, b) => a - b);

  // create a results array
  const results = []; 

  // loop through the nums array
  for (let i = 0; i < nums.length - 3; i++) {
    // check if the index is greater than 0 and the current number is equal to the previous number
    if (i > 0 && nums[i] === nums[i - 1]) {
      // continue
      continue;
    }

    // loop through the nums array
    for (let j = i + 1; j < nums.length - 2; j++) {
      // check if the index is greater than 1 and the current number is equal to the previous number
      if (j > i + 1 && nums[j] === nums[j - 1]) {
        // continue
        continue;
      }

      // create a left pointer
      let left = j + 1;

      // create a right pointer
      let right = nums.length - 1;

      // loop while the left pointer is less than the right pointer
      while (left < right) {
        // create a sum variable
        const sum = nums[i] + nums[j] + nums[left] + nums[right];

        // check if the sum is equal to the target
        if (sum === target) {
          // push the numbers to the results
          results.push([nums[i], nums[j], nums[left], nums[right]]);

          // increment the left pointer
          left++;

          // decrement the right pointer
          right--;

          // loop while the left pointer is less than the right pointer and the left number is equal to the previous number
          while (left < right && nums[left] === nums[left - 1]) {
            // increment the left pointer
            left++;
          }

          // loop while the left pointer is less than the right pointer and the right number is equal to the previous number
          while (left < right && nums[right] === nums[right + 1]) {
            // decrement the right pointer
            right--;
          }
        } else if (sum < target) {
          // increment the left pointer
          left++;
        } else {
          // decrement the right pointer
          right--;
        }
      }
    }
  }

  // return the results array
  return results;
};