/*
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
*/
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findLeastNumOfUniqueInts = function(arr, k) {
    const map = new Map();
    for (let i = 0; i < arr.length; i++) {
        const num = arr[i];
        if (map.has(num)) {
            map.set(num, map.get(num) + 1);
        } else {
            map.set(num, 1);
        }
    }
    const sorted = Array.from(map).sort((a, b) => a[1] - b[1]);
    let count = 0;
    for (let i = 0; i < sorted.length; i++) {
        const num = sorted[i][0];
        const freq = sorted[i][1];
        if (k >= freq) {
            k -= freq;
            count++;
        } else {
            break;
        }
    }
    return sorted.length - count;
};

const arr = [5,5,4], k = 1;
console.log(findLeastNumOfUniqueInts(arr, k)); // 1