    /*
    You are given a 0-indexed array nums consisting of positive integers.

    There are two types of operations that you can apply on the array any number of times:

    Choose two elements with equal values and delete them from the array.
    Choose three elements with equal values and delete them from the array.
    Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
    */

/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
  // sort array nums
  nums.sort((a, b) => a - b);

  // check if numbers contains a number that appears only once
  let unique = false;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1] && nums[i] !== nums[i + 1]) {
      unique = true;
      return -1;
    }
  }

  // count each number's frequency
  let count = {};
  for (let i = 0; i < nums.length; i++) {
    if (!count[nums[i]]) {
      count[nums[i]] = 1;
    } else {
      count[nums[i]]++;
    }
  }


  let result = 0;

  Object.keys(count).forEach(key => {
    let remainingAfter3 = 0;

    const times3 = Math.floor(count[key] / 3);
    if (count[key] % 3 === 1) {
      result += times3 - 1;
      remainingAfter3 = (count[key] % 3) + 3;
    } else {
      result += times3;
      remainingAfter3 = count[key] % 3;
    }

    const times2 = Math.floor(remainingAfter3 / 2);
    result += times2;
  });

  return result;
};