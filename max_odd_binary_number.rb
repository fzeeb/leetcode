=begin
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
=end
# @param {String} s
# @return {String}
def maximum_odd_binary_number(s)
  s = s.split('')
  s.sort! { |a, b| b <=> a }
  s.each_with_index do |n, i|
    if n == '0'
      s[i - 1] = '0'
      break
    end
  end
  s[s.length - 1] = '1'
  return s = s.join('')
end