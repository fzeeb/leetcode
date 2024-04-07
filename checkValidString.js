/*
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Constraints:

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.
*/
/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function(s) {
    let low = 0;
    let high = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            low++;
            high++;
        } else if (s[i] === ')') {
            low--;
            high--;
        } else {
            low--;
            high++;
        }
        if (high < 0) {
            return false;
        }
        low = Math.max(low, 0);
    }
    return low === 0;
};

let s = "()";
console.log(checkValidString(s)); // true