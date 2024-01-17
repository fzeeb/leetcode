/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
  let map = new Map();
  let set = new Set();
  for (let i = 0; i < arr.length; i++) {
    if (map.has(arr[i])) {
      map.set(arr[i], map.get(arr[i]) + 1);
    } else {
      map.set(arr[i], 1);
    }
  }
  for (let [key, value] of map) {
    if (set.has(value)) {
      return false;
    } else {
      set.add(value);
    }
  }
  return true;
};

const arr = [1,2,2,1,1,3];  
console.log(uniqueOccurrences(arr)); // true