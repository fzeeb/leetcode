/*
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
*/
var findDuplicates = function(nums) {
  let duplicates = [];
  const n = nums.length;
  
  for (let i = 0; i < n; i++) {
    const index = Math.abs(nums[i]) - 1;
    
    if (nums[index] < 0) {
      duplicates.push(Math.abs(nums[i]));
    } else {
      nums[index] = -nums[index];
    }
  }
  
  return duplicates;
};