=begin
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
=end
# @param {String[]} words
# @return {String[]}
def common_chars(words)
    result = []
    words[0].each_char do |c|
      if words.all? { |word| word.count(c) > 0 }
        result << c
        words.each do |word|
          word.sub!(c, "")
        end
      end
    end
    result
end

print common_chars(["bella","label","roller"]) # ["e","l","l"]
print common_chars(["cool","lock","cook"]) # ["c","o"]