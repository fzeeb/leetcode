/*
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.
*/
/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {
    let n = heights.length;
    let pq = new PriorityQueue();
    for (let i = 0; i < n - 1; i++) {
      let d = heights[i + 1] - heights[i];
      if (d > 0) {
        pq.push(d);
        if (pq.size() > ladders) {
          bricks -= pq.pop();
        }
        if (bricks < 0) {
          return i;
        }
      }
    }
    return n - 1;
};

class PriorityQueue {
  constructor() {
    this.data = [];
  }

  push(val) {
    this.data.push(val);
    this.data.sort((a, b) => a - b);
  }

  pop() {
    return this.data.shift();
  }

  size() {
    return this.data.length;
  }
}

const heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1;
console.log(furthestBuilding(heights, bricks, ladders)); //4

/*
const heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2;
console.log(furthestBuilding(heights, bricks, ladders)); //7

const heights = [14,3,19,3], bricks = 17, ladders = 0;
console.log(furthestBuilding(heights, bricks, ladders)); //3

const heights = [1,5,1,2,3,4,10000], bricks = 4, ladders = 1;
console.log(furthestBuilding(heights, bricks, ladders)); //5
*/