/*
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
*/

/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    // create an array of 0s with length equal to the length of temperatures
    let answer = Array(temperatures.length).fill(0);
    // create a stack
    let stack = [];
    
    // loop through temperatures
    for (let i = 0; i < temperatures.length; i++) {
        // while stack is not empty and the current temperature is greater than the temperature at the index of the top of the stack
        while (stack.length && temperatures[i] > temperatures[stack[stack.length - 1]]) {
            // pop the top of the stack and set the value at the index of the popped element to the difference between the current index and the popped element
            let index = stack.pop();
            answer[index] = i - index;
        }
        // push the current index to the stack
        stack.push(i);
    }
    
    return answer;
};

const temperatures = [73,74,75,71,69,72,76,73];
console.log(dailyTemperatures(temperatures)); //[1,1,4,2,1,1,0,0]