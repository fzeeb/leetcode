=begin
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.
=end
# @param {Integer[]} nums
# @return {Integer[]}
def find_duplicates(nums)
    duplicates = []
    nums.each do |num|
        if nums[num.abs - 1] < 0
            duplicates.push(num.abs)
        else
            nums[num.abs - 1] *= -1
        end
    end
    duplicates
end