/*
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
*/


/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {  
      let map = {};
      let start = 0;
      let minLen = Infinity;
      let minStart = 0;
      let counter = t.length;
      
      for (let i = 0; i < t.length; i++) {
          if (map[t[i]] === undefined) {
              map[t[i]] = 1;
          } else {
              map[t[i]]++;
          }
      }
      
      for (let end = 0; end < s.length; end++) {
          if (map[s[end]] > 0) {
              counter--;
          }
          map[s[end]]--;
          
          while (counter === 0) {
              if (end - start < minLen) {
                  minStart = start;
                  minLen = end - start;
              }
              map[s[start]]++;
              if (map[s[start]] > 0) {
                  counter++;
              }
              start++;
          }
      }
      
      return minLen === Infinity ? "" : s.substring(minStart, minStart + minLen + 1);
};

const s = "ADOBECODEBANC", t = "ABC";
console.log(minWindow(s, t)); // "BANC"