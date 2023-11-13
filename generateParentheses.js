/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    // create a result array
    let result = [];

    // create a recursive function that takes in a string and the number of open parens
    let recurse = (str, open) => {
        // if the string length is equal to n * 2
        if (str.length === n * 2) {
            // push the string into the result array
            result.push(str);
            // return
            return;
        }

        // if the number of open parens is less than n
        if (open < n) {
            // call the recursive function with the string + ( and open + 1
            recurse(str + '(', open + 1);
        }

        // if the number of open parens is greater than the number of closed parens
        if (open > str.length - open) {
            // call the recursive function with the string + ) and open
            recurse(str + ')', open);
        }
    }

    // call the recursive function with an empty string and 0
    recurse('', 0);

    // return the result array
    return result;
};