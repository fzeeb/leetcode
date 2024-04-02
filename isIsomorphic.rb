=begin
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
=end
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
    return false if s.length != t.length
    hash = {}
    hash2 = {}
    (0...s.length).each do |i|
        if hash[s[i]].nil? && hash2[t[i]].nil?
            hash[s[i]] = t[i]
            hash2[t[i]] = s[i]
        else
            return false if hash[s[i]] != t[i] || hash2[t[i]] != s[i]
        end
    end
    return true
end