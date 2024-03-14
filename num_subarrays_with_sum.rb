=begin
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.
=end
# @param {Integer[]} nums
# @param {Integer} goal
# @return {Integer}
def num_subarrays_with_sum(nums, goal)
  count = 0
  sum = 0
  hash = {0 => 1}

  nums.each do |num|
    sum += num
    count += hash[sum - goal] if hash[sum - goal]
    hash[sum] = hash[sum] ? hash[sum] + 1 : 1
  end
  
  count
end

puts num_subarrays_with_sum([1,0,1,0,1], 2) # 4
puts num_subarrays_with_sum([0,0,0,0,0], 0) # 15