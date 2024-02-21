/*
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
*/
/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var rangeBitwiseAnd = function(left, right) {
    let shift = 0;
    while (left < right) {
        left >>= 1;
        right >>= 1;
        shift++;
    }
    return left << shift;
};

const left = 5, right = 7;
console.log(rangeBitwiseAnd(left, right)); // 4