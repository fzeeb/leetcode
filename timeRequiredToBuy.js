/*
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Constraints:

    n == tickets.length
    1 <= n <= 100
    1 <= tickets[i] <= 100
    0 <= k < n
*/
/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function(tickets, k) {
    let n = tickets.length;
    let time = 0;
    let queue = [];
    for (let i = 0; i < n; i++) {
      queue.push([tickets[i], i]);
    }
    while (queue.length > 0) {
      let [ticket, index] = queue.shift();
      if (ticket > 1) {
        queue.push([ticket - 1, index]);
      }
      if (index === k && ticket === 1) {
        return time + 1;
      }
      time++;
    }
    return time;
};

let tickets = [2,3,2], k = 2
console.log(timeRequiredToBuy(tickets, k)) // 6