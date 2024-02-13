/*
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
*/
/**
 * @param {string[]} words
 * @return {string}
 */
var firstPalindrome = function(words) {
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let palindrom = word.split('').reverse().join('');
    if (word === palindrom) {
      return word;
    }
  }
  return "";
};

const words = ["abc","car","ada","racecar","cool"];
console.log(firstPalindrome(words)); // ada