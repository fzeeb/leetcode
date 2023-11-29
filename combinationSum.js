/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
  // helper function to find all combinations
  function findCombinations(candidates, target, start, combination, result) {
    if (target === 0) {
      result.push(combination.slice());
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] <= target) {
        combination.push(candidates[i]);
        findCombinations(candidates, target - candidates[i], i, combination, result);
        combination.pop();
      }
    }
  }
  
  // call helper function to find all combinations
  let result = [];
  findCombinations(candidates, target, 0, [], result);
  return result;
};