=begin
You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
=end
# @param {String} order
# @param {String} s
# @return {String}
def custom_sort_string(order, s)
  s.chars.sort_by { |c| order.index(c) || 26 }.join
end