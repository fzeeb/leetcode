/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {

  // helper function to check if a string is a palindrome
  function isPalindrome(str) {
    let left = 0;
    let right = str.length - 1;
    while (left < right) {
      if (str[left] !== str[right]) {
        return false;
      }
      left++;
      right--;
    }
    return true;
  }
    
  // check if string is empty
  if (s.length === 0) {
      return "";
  }

  // check if string is 1 character long
  if (s.length === 1) {
      return s;
  }

  // create a variable to store the longest palindrome
  let longestPalindrome = "";

  // loop through the string
  for (let i = 0; i < s.length; i++) {
      // create a variable to store the current palindrome
      let currentPalindrome = "";

      // loop through the string again
      for (let j = i; j < s.length; j++) {
          // add the current character to the current palindrome
          currentPalindrome += s[j];

          // check if the current palindrome is a palindrome
          if (isPalindrome(currentPalindrome)) {
              // check if the current palindrome is longer than the longest palindrome
              if (currentPalindrome.length > longestPalindrome.length) {
                  // update the longest palindrome
                  longestPalindrome = currentPalindrome;
              }
          }
      }
  }

  // return the longest palindrome
  return longestPalindrome;
};