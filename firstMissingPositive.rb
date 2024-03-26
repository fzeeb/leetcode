=begin
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
=end
# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
    n = nums.length
    for i in 0..n-1
        while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        end
    end
    for i in 0..n-1
        if nums[i] != i + 1
            return i + 1
        end
    end
    return n + 1
end