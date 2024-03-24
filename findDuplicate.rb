=begin
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
=end
# @param {Integer[]} nums
# @return {Integer}
def find_duplicate(nums)
    nums.sort!
    for i in 0...nums.length
        if nums[i] == nums[i+1]
            return nums[i]
        end
    end
end