/*
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Hint 1: Assume the problem is to check whether you can reach the last building or not.

Hint 2: You'll have to do a set of jumps, and choose for each one whether to do it using a ladder or bricks. It's always optimal to use ladders in the largest jumps.

Hint 3: Iterate on the buildings, maintaining the largest r jumps and the sum of the remaining ones so far, and stop whenever this sum exceeds b.
*/
/**
 * @param {number[]} heights
 * @param {number} bricks
 * @param {number} ladders
 * @return {number}
 */
var furthestBuilding = function(heights, bricks, ladders) {
    let queue = new PriorityQueue();
    for (let i = 0; i < heights.length; i++) {
      if (i === heights.length - 1) {
        return i;
      }
      if (heights[i] >= heights[i + 1]) {
        continue;
      }
      const diff = heights[i + 1] - heights[i];
      queue.enqueue(diff);
      if (bricks >= diff) {
        bricks -= diff;
      } else if (ladders > 0) {
        bricks += queue.max();
        queue.dequeue();
        ladders--;
        bricks -= diff;
      } else {
        return i;
      }
    }
  };

class PriorityQueue {
  constructor() {
    this.heap = [];
  }

  enqueue(value) {
    this.heap.push(value);
    this.bubbleUp(this.heap.length - 1);
  }

  dequeue() {
    const max = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this.sinkDown(0);
    }
    return max;
  }

  bubbleUp(index) {
    const value = this.heap[index];
    while (index > 0) {
      const parentIndex = Math.floor((index + 1) / 2) - 1;
      const parent = this.heap[parentIndex];
      if (value <= parent) {
        break;
      }
      this.heap[parentIndex] = value;
      this.heap[index] = parent;
      index = parentIndex;
    }
  }

  sinkDown(index) {
    const length = this.heap.length;
    const value = this.heap[index];
    while (true) {
      const rightIndex = (index + 1) * 2;
      const leftIndex = rightIndex - 1;
      let left, right;
      let swap = null;
      if (leftIndex < length) {
        left = this.heap[leftIndex];
        if (left > value) {
          swap = leftIndex;
        }
      }
      if (rightIndex < length) {
        right = this.heap[rightIndex];
        if ((swap === null && right > value) || (swap !== null && right > left)) {
          swap = rightIndex;
        }
      }
      if (swap === null) {
        break;
      }
      this.heap[index] = this.heap[swap];
      this.heap[swap] = value;
      index = swap;
    }
  }

  max() {
    return this.heap[0];
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