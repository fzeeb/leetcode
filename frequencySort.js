/*
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
*/

/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    const map = new Map();
    for (let i = 0; i < s.length; i++) {
        if (map.has(s[i])) {
            map.set(s[i], map.get(s[i]) + 1);
        } else {
            map.set(s[i], 1);
        }
    }
    const sortedMap = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));
    let result = "";
    for (let [key, value] of sortedMap) {
        result += key.repeat(value);
    }
    return result;
};

const s = "tree";
console.log(frequencySort(s)); // "eert" or "eetr" are also valid answers.