/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
  // initialize left and right pointers
  let left = 0;
  let right = nums.length - 1;

  // calculate middle index
  let middle = Math.floor((left + right) / 2);

  // loop through array
  while (left <= right) {
    // if target is found return index
    if (target === nums[middle]) {
      return middle;
    } 
    // if target is less than middle, move right pointer to the left
    else if (target < nums[middle]) {
      right = middle - 1;
    } 
    // if target is greater than middle, move left pointer to the right
    else if (target > nums[middle]) {
      left = middle + 1;
    }
    // recalculate middle index
    middle = Math.floor((left + right) / 2);
  }
  // if target is not found, return left pointer
  return left;

};