/*
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {
    const map = {};
    let missing = 0;
    let duplicate = 0;
    for (let i = 0; i < nums.length; i++) {
        if (map[nums[i]]) {
            duplicate = nums[i];
        } else {
            map[nums[i]] = true;
        }
    }
    for (let i = 1; i <= nums.length; i++) {
        if (!map[i]) {
            missing = i;
            break;
        }
    }
    return [duplicate, missing];
};

const nums = [1,2,2,4];
console.log(findErrorNums(nums)); // [2,3]