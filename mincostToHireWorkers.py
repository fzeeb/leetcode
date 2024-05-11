"""
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the i^th worker and wage[i] is the minimum wage expectation for the i^th worker.
We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:
    Every worker in the paid group must be paid at least their minimum wage expectation.
    In the group, each worker's pay must be directly proportional to their quality. This means if a worker’s quality is double that of another worker in the group, then they must be paid twice as much as the other worker.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example 2:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

Constraints:
    n == quality.length == wage.length
    1 <= k <= n <= 10^4
    1 <= quality[i], wage[i] <= 10^4
"""
from typing import List
import heapq
class Solution:
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    # Create a list of workers with (wage-to-quality ratio, quality)
    workers = []
    for i in range(len(quality)):
      ratio = wage[i] / quality[i]
      workers.append((ratio, quality[i]))
    
    # Sort workers by the wage-to-quality ratio
    workers.sort()

    # Priority queue (max-heap) to store the largest qualities considered so far
    quality_heap = []
    sum_quality = 0
    min_cost = float('inf')

    # Process each worker sorted by their ratio
    for ratio, quality in workers:
      # Add the current worker's quality to the heap and update sum_quality
      heapq.heappush(quality_heap, -quality)
      sum_quality += quality
      
      # Ensure the heap has at most k elements
      if len(quality_heap) > k:
        removed_quality = heapq.heappop(quality_heap)
        sum_quality += removed_quality  # Add since it was negated initially
      
      # If there are exactly k workers, compute the cost
      if len(quality_heap) == k:
        current_cost = sum_quality * ratio
        min_cost = min(min_cost, round(current_cost, 5))

    # Return the computed minimum cost
    return min_cost

print(Solution().mincostToHireWorkers([10,20,5], [70,50,30], 2)) # 105.00000
print(Solution().mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3)) # 30.66667