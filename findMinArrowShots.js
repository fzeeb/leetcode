/*
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
*/
/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
  if (points.length === 0) {
    return 0;
  }
  
  // Sort the balloons based on their end position
  points.sort((a, b) => a[1] - b[1]);
  
  let arrows = 1;
  let end = points[0][1];
  
  // Iterate through the balloons
  for (let i = 1; i < points.length; i++) {
    // If the current balloon starts after the previous balloon ends, we need an additional arrow
    if (points[i][0] > end) {
      arrows++;
      end = points[i][1];
    }
  }
  
  return arrows;
};

let points = [[10,16],[2,8],[1,6],[7,12]];
console.log(findMinArrowShots(points));