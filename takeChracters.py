"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.
Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.

Constraints:
1 <= s.length <= 10^5
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length

Hint 1
Start by counting the frequency of each character and checking if it is possible.

Hint 2
If you take x characters from the left side, what is the minimum number of characters you need to take from the right side? Find this for all values of x in the range 0 ≤ x ≤ s.length.

Hint 3
Use a two-pointers approach to avoid computing the same information multiple times.
"""
from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        # Step 1: Count the frequency of each character in the string
        freq = Counter(s)
        print(f'freq: {freq}')

        # Step 2: If any character has fewer than k occurrences, return -1
        if any(freq[char] < k for char in "abc"):
            return -1

        # Step 3: Calculate the needed frequency for each character to be removed
        n = len(s)
        needed = {char: freq[char] - k for char in "abc"}
        current_window = Counter()
        print(f'needed: {needed}')

        l = 0
        max_valid_window = 0

        # Step 4: Use a sliding window to find the largest valid window that retains enough characters
        for r in range(n):
            current_window[s[r]] += 1

            # If the window becomes invalid, shrink it from the left
            while any(current_window[char] > needed[char] for char in "abc"):
                current_window[s[l]] -= 1
                l += 1

            # Update the maximum valid window size
            max_valid_window = max(max_valid_window, r - l + 1)

        # Step 5: The minimum time is the complement of the largest valid window
        return n - max_valid_window


# Test Cases
s = Solution()
print(s.takeCharacters("aabaaaacaabc", 2))  # Expected: 8
print(s.takeCharacters("a", 1))  # Expected: -1
print(s.takeCharacters("a", 0))  # Expected: 0
print(s.takeCharacters("aabbccca", 2))  # Expected: 6