/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  let map = new Map();
  map.set(1, 1);
  map.set(2, 2);
  for (let i = 3; i <= n; i++) {
    map.set(i, map.get(i-1) + map.get(i-2));
    console.log(map);
  }
  return map.get(n);
};

const n = 10;
console.log(climbStairs(n)); // 2