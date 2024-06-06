=begin
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the i^th card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:
    1 <= hand.length <= 10^4
    0 <= hand[i] <= 10^9
    1 <= groupSize <= hand.length
=end
# @param {Integer[]} hand
# @param {Integer} group_size
# @return {Boolean}
def is_n_straight_hand(hand, group_size)
  return false if hand.length % group_size != 0
  hand.sort!
  while hand.length > 0
    card = hand.shift
    (1...group_size).each do |i|
      if hand.include?(card+i)
        hand.delete_at(hand.index(card+i))
      else
        return false
      end
    end
  end
  true
end

puts is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) # true
puts is_n_straight_hand([1, 2, 3, 4, 5], 4) # false