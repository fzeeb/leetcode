=begin
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    0 <= limit <= 10^9

Hint 1
Use a sliding window approach keeping the maximum and minimum value using a data structure like a multiset from STL in C++.

Hint 2
More specifically, use the two pointer technique, moving the right pointer as far as possible to the right until the subarray is not valid (maxValue - minValue > limit), then moving the left pointer until the subarray is valid again (maxValue - minValue <= limit). Keep repeating this process.
=end
# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer}
def longest_subarray(nums, limit)
  maxd = []
  mind = []
  left = 0
  for right in 0...nums.length
    num = nums[right]
    while !maxd.empty? && num > maxd[-1]
      maxd.pop
    end
    while !mind.empty? && num < mind[-1]
      mind.pop
    end
    maxd.push(num)
    mind.push(num)
    if maxd[0] - mind[0] > limit
      if maxd[0] == nums[left]
        maxd.shift
      end
      if mind[0] == nums[left]
        mind.shift
      end
      left += 1
    end
  end
  return right - left + 1
end

puts longest_subarray([8,2,4,7], 4) #2
puts longest_subarray([10,1,2,4,7,2], 5) #4
puts longest_subarray([4,2,2,2,4,4,2,2], 0) #3