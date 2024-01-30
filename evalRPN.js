/*
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.
*/

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    let stack = [];
    
    for (let i = 0; i < tokens.length; i++) {
        if (tokens[i] === "+") {
            stack.push(stack.pop() + stack.pop());
        } else if (tokens[i] === "-") {
            stack.push(-stack.pop() + stack.pop());
        } else if (tokens[i] === "*") {
            stack.push(stack.pop() * stack.pop());
        } else if (tokens[i] === "/") {
            let divisor = stack.pop();
            stack.push(Math.trunc(stack.pop() / divisor));
        } else {
            stack.push(parseInt(tokens[i]));
        }
    }
    
    return stack[0];
};

const tokens = ["2","1","+","3","*"];
console.log(evalRPN(tokens)); //9