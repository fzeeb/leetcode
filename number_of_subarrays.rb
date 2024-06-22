=begin
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
    1 <= nums.length <= 50000
    1 <= nums[i] <= 10^5
    1 <= k <= nums.length

Hint 1
After replacing each even by zero and every odd by one can we use prefix sum to find answer ?

Hint 2
Can we use two pointers to count number of sub-arrays ?

Hint 3
Can we store indices of odd numbers and for each k indices count number of sub-arrays contains them ?
=end
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def number_of_subarrays(nums, k)
  odd_indices = []
  nums.each_with_index do |num, index|
    odd_indices << index if num.odd?
  end

  return 0 if odd_indices.size < k

  count = 0
  odd_indices.each_with_index do |odd_index, index|
    next if index + k > odd_indices.size

    left = index > 0 ? odd_indices[index - 1] + 1 : 0
    right = index + k < odd_indices.size ? odd_indices[index + k] : nums.size

    left_count = odd_index - left + 1
    right_count = right - odd_indices[index + k - 1]

    count += left_count * right_count
  end

  count
end

puts number_of_subarrays([1,1,2,1,1], 3) == 2
puts number_of_subarrays([2,4,6], 1) == 0
puts number_of_subarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16