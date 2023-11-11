// Description: Unit tests for 3sumClosest.js
const threeSumClosest = require('./3sumClosest.js');

// Test Case 1
let nums = [-1,2,1,-4];
let target = 1;
let expectedOutput = 2;
let result = threeSumClosest(nums, target);
console.log(result === expectedOutput); // true

// Test Case 2
nums = [0,0,0];
target = 1;
expectedOutput = 0;
result = threeSumClosest(nums, target);
console.log(result === expectedOutput); // true

// Test Case 3
nums = [1,2,3,4,5];
target = 10;
expectedOutput = 12;
result = threeSumClosest(nums, target);
console.log(result === expectedOutput); // true

// Test Case 4
nums = [-2,0,1,1,2];
target = 2;
expectedOutput = 2;
result = threeSumClosest(nums, target);
console.log(result === expectedOutput); // true