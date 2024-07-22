=begin
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.
For each index i, names[i] and heights[i] denote the name and height of the i^th person.
Return names sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Constraints:
    n == names.length == heights.length
    1 <= n <= 10^3
    1 <= names[i].length <= 20
    1 <= heights[i] <= 10^5
    names[i] consists of lower and upper case English letters.
    All the values of heights are distinct.

Hint 1
Find the tallest person and swap with the first person, then find the second tallest person and swap with the second person, etc. Repeat until you fix all n people.
=end
# @param {String[]} names
# @param {Integer[]} heights
# @return {String[]}
def sort_people(names, heights)
  n = names.length
  for i in 0..n-1
    for j in i+1..n-1
      if heights[i] < heights[j]
        heights[i], heights[j] = heights[j], heights[i]
        names[i], names[j] = names[j], names[i]
      end
    end
  end
  names
end

# Test cases
puts sort_people(["Mary","John","Emma"], [180,165,170]).to_s # ["Mary","Emma","John"]
puts sort_people(["Alice","Bob","Bob"], [155,185,150]).to_s # ["Bob","Alice","Bob"]