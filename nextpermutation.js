/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    // create a pointer to the end of the array
    let i = nums.length - 1;
    // iterate through the array from the end
    while (i > 0 && nums[i] <= nums[i - 1]) i--;
    // if i is not 0
    if (i !== 0) {
      // create a pointer to the end of the array
      let j = nums.length - 1;
      // iterate through the array from the end
      while (nums[j] <= nums[i - 1]) j--;
      // swap the values of the two pointers
      swap(nums, i - 1, j);
    } 
    // reverse the array from i to the end
    reverse(nums, i);

    // helper function to swap two values in an array
    function swap(nums, i, j) {
      let temp = nums[i];
      nums[i] = nums[j];
      nums[j] = temp;
    }
    // helper function to reverse an array from i to the end
    function reverse(nums, i) {
      let j = nums.length - 1;
      while (i < j) {
        swap(nums, i, j);
        i++;
        j--;
      }
    }

    // return the array
    return nums;
};