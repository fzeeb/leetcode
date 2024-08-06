=begin
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.
Return the minimum number of pushes needed to type word after remapping the keys.
An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

Example 1:
Input: word = "abcde"
Output: 5
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
Total cost is 1 + 1 + 1 + 1 + 1 = 5.
It can be shown that no other mapping can provide a lower cost.

Example 2:
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.

Example 3:
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.

Constraints:
    1 <= word.length <= 10^5
    word consists of lowercase English letters.

Hint 1
We have 8 keys in total. We can type 8 characters with one push each, 8 different characters with two pushes each, and so on.

Hint 2
The optimal way is to map letters to keys evenly.

Hint 3
Sort the letters by frequencies in the word in non-increasing order.
=end
# @param {String} word
# @return {Integer}
def minimum_pushes(word)
  # Step 1: Calculate frequency of each character in the word
  frequency = Hash.new(0)
  word.each_char { |char| frequency[char] += 1 }

  # Step 2: Sort characters by frequency in descending order
  sorted_frequencies = frequency.values.sort.reverse

  # Step 3: Calculate minimum pushes needed
  total_pushes = 0
  sorted_frequencies.each_with_index do |freq, index|
    # Determine the round of key presses based on index
    key_presses = (index / 8) + 1
    total_pushes += freq * key_presses
  end

  total_pushes
end

# Test cases
p minimum_pushes("abcde") == 5
p minimum_pushes("xyzxyzxyzxyz") == 12
p minimum_pushes("aabbccddeeffgghhiiiiii") == 24