/*
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
*/

/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    const result = [];
    for (let i = 1; i <= 9; i++) {
        let num = i;
        for (let j = i + 1; j <= 9; j++) {
            num = num * 10 + j;
            if (num >= low && num <= high) {
                result.push(num);
            }
        }
    }
    return result.sort((a, b) => a - b);
};

const low = 100, high = 300
console.log(sequentialDigits(low, high)); // [123,234]
