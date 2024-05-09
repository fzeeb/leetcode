=begin
You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

Example 1:
Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

Example 2:
Input: happiness = [1,1,1,1], k = 2
Output: 1
Explanation: We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.

Example 3:
Input: happiness = [2,3,4,5], k = 1
Output: 5
Explanation: We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.

Constraints:
    1 <= n == happiness.length <= 2 * 10^5
    1 <= happiness[i] <= 10^8
    1 <= k <= n

Hint 1
Since all the unselected numbers are decreasing at the same rate, we should greedily select k largest values.

Hint 2
The i^th largest number (i = 1, 2, 3,…k) should decrease by (i - 1) when it is picked.

Hint 3
Add 0 if the decreased value is negative.
=end
# @param {Integer[]} happiness
# @param {Integer} k
# @return {Integer}
def maximum_happiness_sum(happiness, k)
  t = 0
  max_happiness = 0
  happiness = happiness.sort.reverse
  k.times do
    t += 1
    break if happiness[0] <= 0
    max_happiness += happiness.shift
    if happiness[0] <= 0
      happiness[0] -= t
    end
  end
  max_happiness
end

puts maximum_happiness_sum([1,2,3], 2) == 4
puts maximum_happiness_sum([1,1,1,1], 2) == 1
puts maximum_happiness_sum([2,3,4,5], 1) == 5