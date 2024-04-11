/*
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Constraints:

    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
*/
/**
 * @param {string} num
 * @param {number} k
 * @return {string}
 */
var removeKdigits = function(num, k) {
    let stack = [];
    num = num.toString();
    for (let i = 0; i < num.length; i++) {
        while (stack.length > 0 && k > 0 && stack[stack.length - 1] > num[i]) {
            stack.pop();
            k--;
        }
        stack.push(num[i]);
    }
    while (k > 0) {
        stack.pop();
        k--;
    }
    let result = stack.join('').replace(/^0+/, '');
    return result.length > 0 ? result : '0';
};

console.log(removeKdigits(1432219, 3)); // Output: "1219"
console.log(removeKdigits(10200, 1)); // Output: "200"
console.log(removeKdigits(10, 2)); // Output: "0"