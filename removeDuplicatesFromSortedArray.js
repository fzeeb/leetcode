/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  // remove dupliacates using in-place algorithm
  // create a pointer at index 0
  let pointer = 0;
  // loop through the nums array
  for (let i = 0; i < nums.length; i++) {
    // if the current element is not equal to the element at the pointer
    if (nums[i] !== nums[pointer]) {
      // increment the pointer
      pointer++;
      // set the element at the pointer to the current element
      nums[pointer] = nums[i];
    }
  }
  // return the pointer + 1
  return pointer + 1;
};