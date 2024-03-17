=begin
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
=end
# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
  result = []
  i = 0
  while i < intervals.length && intervals[i][1] < new_interval[0]
    result << intervals[i]
    i += 1
  end
  while i < intervals.length && intervals[i][0] <= new_interval[1]
    new_interval[0] = [new_interval[0], intervals[i][0]].min
    new_interval[1] = [new_interval[1], intervals[i][1]].max
    i += 1
  end
  result << new_interval
  while i < intervals.length
    result << intervals[i]
    i += 1
  end
  result 
end

intervals = [[1,3],[6,9]], newInterval = [2,5]
puts insert(intervals, newInterval) # [[1,5],[6,9]]