/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    // remove all instances of val in-place
    // create a pointer at index 0
    let pointer = 0;
    // loop through the nums array
    for (let i = 0; i < nums.length; i++) {
      // if the current element is not equal to val
      if (nums[i] !== val) {
        // set the element at the pointer to the current element
        nums[pointer] = nums[i];
        // increment the pointer
        pointer++;
      }
    }
    // return the pointer
    return pointer;
};