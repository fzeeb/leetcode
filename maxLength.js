/*
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
*/
/**
 * @param {string[]} arr
 * @return {number}
 */
var maxLength = function(arr) {
    let max = 0;
    const dfs = (index, str) => {
        if (index === arr.length) {
            max = Math.max(max, str.length);
            return;
        }
        const newStr = str + arr[index];
        if (new Set(newStr).size === newStr.length) {
            dfs(index + 1, newStr);
        }
        dfs(index + 1, str);
    }
    dfs(0, "");
    return max;  
};

const arr = ["un","iq","ue"]
console.log(maxLength(arr)); // 4