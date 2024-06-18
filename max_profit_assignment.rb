=begin
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:
    difficulty[i] and profit[i] are the difficulty and the profit of the i^th job, and
    worker[j] is the ability of j^th worker (i.e., the j^th worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.
    For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0

Constraints:
    n == difficulty.length
    n == profit.length
    m == worker.length
    1 <= n, m <= 10^4
    1 <= difficulty[i], profit[i], worker[i] <= 10^5
=end
# @param {Integer[]} difficulty
# @param {Integer[]} profit
# @param {Integer[]} worker
# @return {Integer}
def max_profit_assignment(difficulty, profit, worker)
  # Combine difficulty and profit into a list of jobs and sort them by difficulty
  jobs = difficulty.zip(profit).sort_by { |d, p| d }
  worker.sort!

  max_profit = 0
  best_profit = 0
  job_index = 0

  # Iterate over each worker
  worker.each do |ability|
    # Update the best profit for jobs that the current worker can do
    while job_index < jobs.size && jobs[job_index][0] <= ability
      best_profit = [best_profit, jobs[job_index][1]].max
      job_index += 1
    end
    # Add the best profit the worker can achieve to the max_profit
    max_profit += best_profit
  end

  # Return the total maximum profit
  max_profit
end

# Test cases
puts max_profit_assignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]) # 100
puts max_profit_assignment([85,47,57], [24,66,99], [40,25,25]) # 0
puts max_profit_assignment([66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63], [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77], [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]) # 1392