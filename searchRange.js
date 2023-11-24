/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
  // initalize result
  let result = []

  // find first position of target
  result.push(nums.indexOf(target))

  // find ending position of target
  result.push(nums.lastIndexOf(target))

  return result
};