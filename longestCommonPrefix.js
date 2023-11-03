/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
  // check if input array is empty
  if (strs.length === 0) {
    return '';
  }
  // initialize prefix
  let prefix = '';
  // initialize index
  let index = 0;
  // initialize currentChar
  let currentChar;
  // while currentChar is the same for each string
  while (true) {
    // check if index is out of bounds for any string
    if (index >= strs[0].length) {
      return prefix;
    }
    currentChar = strs[0][index];
    for (let i = 1; i < strs.length; i++) {
      // check if index is out of bounds for any string or if current string is empty
      if (index >= strs[i].length || strs[i][index] !== currentChar) {
        return prefix;
      }
    }
    prefix += currentChar;
    index++;
  }
};