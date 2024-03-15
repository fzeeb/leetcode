=begin
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
=end
# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
  n = nums.length
  output = Array.new(n, 1)
  left = 1
  right = 1
  
  (0...n).each do |i|
    output[i] *= left
    output[n - 1 - i] *= right
    left *= nums[i]
    right *= nums[n - 1 - i]
  end
  
  output 
end

nums = [1,2,3,4]
puts product_except_self(nums) # [24,12,8,6]