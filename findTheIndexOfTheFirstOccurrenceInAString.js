/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
  // if needle is empty return 0
  if (needle === '') return 0;
  // if needle is not in haystack return -1
  if (haystack.indexOf(needle) === -1) return -1;
  // if needle is in haystack return the index of the first occurrence
  return haystack.indexOf(needle);
};