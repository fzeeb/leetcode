// Description: Unit tests for 3sum.js
// import { threeSum } from './3sum.js';
const threeSum = require('./3sum.js');

// Test Case 1
let nums = [-1,0,1,2,-1,-4];
let expectedOutput = [[-1,-1,2],[-1,0,1]];
let result = threeSum(nums);
console.log(JSON.stringify(result) === JSON.stringify(expectedOutput)); // true

// Test Case 2
nums = [0,0,0];
expectedOutput = [[0,0,0]];
result = threeSum(nums);
console.log(JSON.stringify(result) === JSON.stringify(expectedOutput)); // true

// Test Case 3
nums = [1,2,3,4,5];
expectedOutput = [];
result = threeSum(nums);
console.log(JSON.stringify(result) === JSON.stringify(expectedOutput)); // true

// Test Case 4
nums = [-2,0,1,1,2];
expectedOutput = [[-2,0,2],[-2,1,1]];
result = threeSum(nums);
console.log(JSON.stringify(result) === JSON.stringify(expectedOutput)); // true