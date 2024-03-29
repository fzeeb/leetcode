=begin
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
=end
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def get_common(nums1, nums2)
  common_elements = nums1 & nums2
  common_elements.empty? ? -1 : common_elements.min
end

# Example 1
nums1 = [1,2,3]
nums2 = [2,4]
puts get_common(nums1, nums2) # 2