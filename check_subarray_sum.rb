=begin
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
    its length is at least two, and
    the sum of the elements of the subarray is a multiple of k.
Note that:
    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    0 <= sum(nums[i]) <= 2^31 - 1
    1 <= k <= 2^31 - 1
=end
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum(nums, k)
  return false if nums.length < 2

  # Initialize the hash map with key 0 and value -1
  sum_mod_k_map = {0 => -1}
  sum = 0

  nums.each_with_index do |num, i|
    sum += num
    sum %= k if k != 0
    if sum_mod_k_map.has_key?(sum)
      return true if i - sum_mod_k_map[sum] > 1
    else
      sum_mod_k_map[sum] = i
    end
  end

  false
end

puts check_subarray_sum([23, 2, 4, 6, 7], 6) # true
puts check_subarray_sum([23, 2, 6, 4, 7], 6) # true
puts check_subarray_sum([23, 2, 6, 4, 7], 13) # false