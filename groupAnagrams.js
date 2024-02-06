/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
*/

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map();
    for (let str of strs) {
        const sorted = str.split('').sort().join('');
        if (map.has(sorted)) {
            map.get(sorted).push(str);
        } else {
            map.set(sorted, [str]);
        }
    }
    return Array.from(map.values());    
};

const strs = ["eat","tea","tan","ate","nat","bat"];
console.log(groupAnagrams(strs)); // [["bat"],["nat","tan"],["ate","eat","tea"]]