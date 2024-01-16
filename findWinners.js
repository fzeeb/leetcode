// You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

/**
 * @param {number[][]} matches
 * @return {number[][]}
 */
var findWinners = function(matches) {
  let answer = [[],[]]
  let map = {};
  
  for (let i = 0; i < matches.length; i++) {
    map[matches[i][0]] = map[matches[i][0]] + 0 || 0;
    map[matches[i][1]] = map[matches[i][1]] + 1 || 1;
  }  
 
  for (let key in map) {
    if (map[key] === 0) {
      answer[0].push(key);
    }
    if (map[key] === 1) {
      answer[1].push(key);
    }
  }

  return answer; 
}

const matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]];
console.log(findWinners(matches)); // [1,2,10],[4,5,7,8]