# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def num_subarray_product_less_than_k(nums, k)
    return 0 if k <= 1
    product = 1
    left = 0
    count = 0
    for right in 0...nums.length
        product *= nums[right]
        while product >= k
            product /= nums[left]
            left += 1
        end
        count += right - left + 1
    end
    count
end