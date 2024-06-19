=begin
You are given an integer array bloomDay, an integer m and an integer k.
You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the i^th flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

Example 2:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.

Example 3:
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.

Constraints:
    bloomDay.length == n
    1 <= n <= 10^5
    1 <= bloomDay[i] <= 10^9
    1 <= m <= 10^6
    1 <= k <= n

Hint 1
If we can make m or more bouquets at day x, then we can still make m or more bouquets at any day y > x.

Hint 2
We can check easily if we can make enough bouquets at day x if we can get group adjacent flowers at day x.
=end
# @param {Integer[]} bloom_day
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_days(bloom_day, m, k)
  return -1 if m * k > bloom_day.size
  left = 1
  right = bloom_day.max
  while left < right
    mid = (left + right) / 2
    if check(bloom_day, m, k, mid)
      right = mid
    else
      left = mid + 1
    end
  end
  left 
end

def check(bloom_day, m, k, mid)
  count = 0
  flowers = 0
  bloom_day.each do |day|
    if day <= mid
      flowers += 1
      if flowers == k
        count += 1
        flowers = 0
      end
    else
      flowers = 0
    end
  end
  count >= m
end

puts min_days([1,10,3,10,2], 3, 1) # 3
puts min_days([1,10,3,10,2], 3, 2) # -1
puts min_days([7,7,7,7,12,7,7], 2, 3) # 12