/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  // create a stack
  const stack = [];

  // create a map of open and close parentheses
  const map = {
    '(': ')',
    '[': ']',
    '{': '}'
  };

  // loop through the string
  for (let i = 0; i < s.length; i++) {
    // check if the current character is an open parentheses
    if (map[s[i]]) {
      // push the current character to the stack
      stack.push(s[i]);
    } else {
      // check if the current character is not equal to the last character in the stack
      if (map[stack.pop()] !== s[i]) {
        // return false
        return false;
      }
    }
  }

  // return true if the stack is empty
  return stack.length === 0;
};