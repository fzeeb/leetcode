// Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const charMap = {};
    for (let i = 0; i < s.length; i++) {
        if (charMap[s[i]] === undefined) {
            charMap[s[i]] = 1;
        } else {
            charMap[s[i]]++;
        }
    }
    for (let i = 0; i < s.length; i++) {
        if (charMap[s[i]] === 1) {
            return i;
        }
    }
    return -1;
};

const s = "leetcode";
console.log(firstUniqChar(s)); // 0