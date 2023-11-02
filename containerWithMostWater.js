/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
  // initialize maxArea
  let maxArea = 0;

  // initialize left and right pointers
  let left = 0;
  let right = height.length - 1;

  // while left is less than right
  while (left < right) {
    // calculate area
    const area = Math.min(height[left], height[right]) * (right - left);
    // if area is greater than maxArea, update maxArea
    if (area > maxArea) {
      maxArea = area;
    }
    // if left is less than right, increment left
    if (height[left] < height[right]) {
      left++;
    // else, decrement right
    } else {
      right--;
    }
  }

  // return maxArea
  return maxArea;
};