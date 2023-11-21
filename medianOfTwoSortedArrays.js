/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
  // combine the two arrays
  let combined = nums1.concat(nums2);
  // sort the combined array
  combined.sort((a, b) => a - b);
  // find the middle index
  let mid = Math.floor(combined.length / 2);
  // if the combined array is even
  if (combined.length % 2 === 0) {
    // return the average of the middle two elements
    return (combined[mid - 1] + combined[mid]) / 2;
  } else {
    // return the middle element
    return combined[mid];
  }
};