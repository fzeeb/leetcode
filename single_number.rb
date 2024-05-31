=begin
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:
Input: nums = [-1,0]
Output: [-1,0]

Example 3:
Input: nums = [0,1]
Output: [1,0]

Constraints:
    2 <= nums.length <= 3 * 10^4
    -2^31 <= nums[i] <= 2^31 - 1
    Each integer in nums will appear twice, only two integers will appear once.
=end
# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
  xor = nums.reduce(0) { |acc, num| acc ^ num }
  mask = 1
  mask = mask << 1 while (mask & xor).zero?
  first = 0
  second = 0
  nums.each do |num|
    if (num & mask).zero?
      first ^= num
    else
      second ^= num
    end
  end
  [first, second]
end

print single_number([1, 2, 1, 3, 2, 5]) # [3, 5]
print single_number([-1, 0]) # [-1, 0]
print single_number([0, 1]) # [1, 0]