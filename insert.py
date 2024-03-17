from typing import List
""" 
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
      result.append(intervals[i])
      i += 1
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
      newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
      i += 1
    result.append(newInterval)
    while i < len(intervals):
      result.append(intervals[i])
      i += 1
    return result
    
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval)) # [[1,5],[6,9]]