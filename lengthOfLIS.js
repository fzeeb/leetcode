// Given an integer array nums, return the length of the longest strictly increasing subsequence

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    // create an array to store the longest increasing subsequence
    const tmp = new Array(nums.length).fill(1);
    let max = 1;
    // loop through the nums array
    for (let i = 1; i < nums.length; i++) {
        // loop through the tmp array
        for (let j = 0; j < i; j++) {
            // if the current number is greater than the previous number
            if (nums[i] > nums[j]) {
                // update the tmp array
                tmp[i] = Math.max(tmp[i], tmp[j] + 1);
            }
        }
        // update the max
        max = Math.max(max, tmp[i]);
    }
    return max;
};

const nums = [10,9,2,5,3,7,101,18]
console.log(lengthOfLIS(nums)) // 4