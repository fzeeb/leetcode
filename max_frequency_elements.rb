=begin
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
=end
# @param {Integer[]} nums
# @return {Integer}
def max_frequency_elements(nums)
  freq = Hash.new(0)
  nums.each { |n| freq[n] += 1 }
  max = freq.values.max
  freq.select { |k, v| v == max }.values.sum
end