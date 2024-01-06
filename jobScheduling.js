/*
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
*/
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number[]} profit
 * @return {number}
 */
var jobScheduling = function(startTime, endTime, profit) {
  // create an array to store the jobs
  const jobs = [];
  // loop through the startTime array
  for (let i = 0; i < startTime.length; i++) {
    // push the startTime, endTime, and profit into the jobs array
    jobs.push([startTime[i], endTime[i], profit[i]]);
  }
  // sort the jobs array by the endTime
  jobs.sort((a, b) => a[1] - b[1]);
  // create an array to store the profit
  const dp = new Array(startTime.length).fill(0);
  dp[0] = jobs[0][2];
  // loop through the jobs array
  for (let i = 1; i < jobs.length; i++) {
    // create a variable to store the current profit
    let currProfit = jobs[i][2];
    // loop through the jobs array
    for (let j = i - 1; j >= 0; j--) {
      // if the endTime of the current job is greater than the startTime of the previous job
      if (jobs[i][0] >= jobs[j][1]) {
        // update the current profit
        currProfit = Math.max(currProfit, jobs[i][2] + dp[j]);
      }
    }
    // update the dp array
    dp[i] = Math.max(currProfit, dp[i - 1]);
  }
  return dp[dp.length - 1];
};  

const startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
console.log(jobScheduling(startTime, endTime, profit)) // 120