=begin
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

Constraints:
    1 <= nums.length <= 5 * 10^4
    -5 * 10^4 <= nums[i] <= 5 * 10^4
=end
# @param {Integer[]} nums
# @return {Integer[]}
def sort_array(nums)
  return nums if nums.length <= 1

    mid = nums.length / 2
    left = sort_array(nums[0...mid])
    right = sort_array(nums[mid..-1])

    merge(left, right)
  end

  def merge(left, right)
    result = []
    left_index = 0
    right_index = 0

    while left_index < left.length && right_index < right.length
      if left[left_index] <= right[right_index]
        result << left[left_index]
        left_index += 1
      else
        result << right[right_index]
        right_index += 1
      end
  end

  result.concat(left[left_index..-1])
  result.concat(right[right_index..-1])
  result
end

# Test cases
puts sort_array([5,2,3,1]).to_s # [1,2,3,5]
puts sort_array([5,1,1,2,0,0]).to_s # [0,0,1,1,2,5]