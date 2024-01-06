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
  const jobs = startTime.map((start, index) => [start, endTime[index], profit[index]]);
  jobs.sort((a, b) => a[1] - b[1]);

  const dp = Array(jobs.length).fill(0);
  dp[0] = jobs[0][2];

  const binarySearch = (i) => {
    let start = 0;
    let end = i - 1;
    while (start <= end) {
      let mid = Math.floor((start + end) / 2);
      if (jobs[mid][1] <= jobs[i][0]) {
        if (jobs[mid + 1][1] <= jobs[i][0]) {
          start = mid + 1;
        } else {
          return mid;
        }
      } else {
        end = mid - 1;
      }
    }
    return -1;
  };

  for (let i = 1; i < jobs.length; i++) {
    let currProfit = jobs[i][2];
    let l = binarySearch(i);
    if (l != -1) {
      currProfit += dp[l];
    }
    dp[i] = Math.max(currProfit, dp[i - 1]);
  }

  return dp[dp.length - 1];
} 

const startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
console.log(jobScheduling(startTime, endTime, profit)) // 120