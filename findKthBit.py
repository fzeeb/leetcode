"""
Given two positive integers n and k, the binary string S_n is formed as follows:

    S_1 = "0"
    S_i = S_i-1 + "1" + reverse(invert(Si - 1)) for i > 1

Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

    S_1 = "0"
    S_2 = "011"
    S_3 = "0111001"
    S_4 = "011100110110001"

Return the k^th bit in S_n. It is guaranteed that k is valid for the given n.

Example 1:
Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1^st bit is "0".

Example 2:
Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11^th bit is "1".

Constraints:

    1 <= n <= 20
    1 <= k <= 2^n - 1

Hint 1
Since n is small, we can simply simulate the process of constructing S1 to S_n.
"""
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
      def invert(s: str) -> str:
        return ''.join('1' if c == '0' else '0' for c in s)

      def reverse(s: str) -> str:
        return s[::-1]

      s = "0"
      for i in range(1, n):
        s = s + "1" + reverse(invert(s))
      
      return s[k-1]
        

# Test Cases
s = Solution()
print(s.findKthBit(3, 1) == "0")
print(s.findKthBit(4, 11) == "1")