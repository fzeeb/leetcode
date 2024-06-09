=begin
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
    1 <= nums.length <= 3 * 10^4
    -104 <= nums[i] <= 10^4
    2 <= k <= 10^4
=end
 # @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_div_by_k(nums, k)
  sum_mod_k_map = {0 => 1}
  sum = 0
  count = 0
  
  nums.each do |num|
    sum += num
    sum %= k
    count += sum_mod_k_map[sum].to_i
    sum_mod_k_map[sum] = sum_mod_k_map[sum].to_i + 1
  end
  
  count   
end

puts subarrays_div_by_k([4, 5, 0, -2, -3, 1], 5) # 7
puts subarrays_div_by_k([5], 9) # 0