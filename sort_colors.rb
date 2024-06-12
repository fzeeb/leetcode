=begin
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function. 

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
    n == nums.length
    1 <= n <= 300
    nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Hint 1
A rather straight forward solution is a two-pass algorithm using counting sort.

Hint 2
Iterate the array counting number of 0's, 1's, and 2's.
=end
# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def sort_colors(nums)
  n = nums.length
  left = 0
  right = n - 1
  i = 0
  while i <= right
    if nums[i] == 0
      nums[i], nums[left] = nums[left], nums[i]
      left += 1
      i += 1
    elsif nums[i] == 2
      nums[i], nums[right] = nums[right], nums[i]
      right -= 1
    else
      i += 1
    end
  end
  nums
end

print sort_colors([2, 0, 2, 1, 1, 0]) # [0, 0, 1, 1, 2, 2]
print sort_colors([2, 0, 1]) # [0, 1, 2]