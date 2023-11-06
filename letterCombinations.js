/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
  // check if the digits is empty
  if (!digits.length) {
    // return an empty array
    return [];
  }

  // create a map of the digits to letters
  const map = {
    2: 'abc', 
    3: 'def', 
    4: 'ghi', 
    5: 'jkl', 
    6: 'mno', 
    7: 'pqrs', 
    8: 'tuv', 
    9: 'wxyz'
  };

  // create a results array
  const results = [];

  // create a helper function to get the combinations
  const getCombinations = (index, combination) => {
    // check if the combination length is equal to the digits length
    if (combination.length === digits.length) {
      // push the combination to the results
      results.push(combination);

      // return
      return;
    }

    // loop through the map at the index
    for (let i = 0; i < map[digits[index]].length; i++) {
      // call the helper function with the index incremented and the combination plus the letter
      getCombinations(index + 1, combination + map[digits[index]][i]);
    }
  };

  // call the helper function with the index and an empty string
  getCombinations(0, '');

  // return the results array
  return results;
};