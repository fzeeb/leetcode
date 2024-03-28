=begin
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
=end
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
  def max_subarray_length(nums, k)
    freq = {}
    left = 0
    max_len = 0

    (0...nums.length).each do |right|
      freq[nums[right]] ||= 0
      freq[nums[right]] += 1

      while freq[nums[right]] > k
        freq[nums[left]] -= 1
        left += 1
      end

      max_len = [max_len, right - left + 1].max
    end

    max_len
  end
