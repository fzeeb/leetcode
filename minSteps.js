/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
  
      let count = 0;
      let map = {};
  
      for (let i = 0; i < s.length; i++) {
          map[s[i]] = map[s[i]] + 1 || 1;
      }
  
      for (let i = 0; i < t.length; i++) {
          if (map[t[i]]) {
              map[t[i]]--;
          } else {
              count++;
          }
      }
      return count;
};

const s = "bab", t = "aba"
console.log(minSteps(s, t));  // 1