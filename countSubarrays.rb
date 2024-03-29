=begin
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.
=end
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_subarrays(nums, k)
  count = 0
  max_num = nums.max
  window_start = 0
  max_count = 0

  (0...nums.length).each do |window_end|
    if nums[window_end] == max_num
      max_count += 1
    end

    while max_count >= k
      count += nums.length - window_end
      if nums[window_start] == max_num
        max_count -= 1
      end
      window_start += 1
    end
  end

  count
end

nums = [1,3,2,3,3]
k = 2
puts count_subarrays(nums, k) # 6ß