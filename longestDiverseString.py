"""
A string s is called happy if it satisfies the following conditions:

    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.

Constraints:
    0 <= a, b, c <= 100
    a + b + c > 0

Hint 1
Use a greedy approach.

Hint 2
Use the letter with the maximum current limit that can be added without breaking the condition.
"""
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        answer = ""
        tmp = ""
        n = a + b + c
        while n > 0:
            if a >= b and a >= c and a > 0:
                if tmp != "aa":
                    answer += "a"
                    a -= 1
                    tmp += "a"
                else:
                    if b > 0:
                        answer += "b"
                        b -= 1
                        tmp = "b"
                    elif c > 0:
                        answer += "c"
                        c -= 1
                        tmp = "c"
            elif b >= a and b >= c and b > 0:
                if tmp != "bb":
                    answer += "b"
                    b -= 1
                    tmp += "b"
                else:
                    if a > 0:
                        answer += "a"
                        a -= 1
                        tmp = "a"
                    elif c > 0:
                        answer += "c"
                        c -= 1
                        tmp = "c"
            elif c >= a and c >= b and c > 0:
                if tmp != "cc":
                    answer += "c"
                    c -= 1
                    tmp += "c"
                else:
                    if a > 0:
                        answer += "a"
                        a -= 1
                        tmp = "a"
                    elif b > 0:
                        answer += "b"
                        b -= 1
                        tmp = "b"

            tmp = tmp[-2:]
            n -= 1
        
        return answer
        

# Test cases
s = Solution()
print(s.longestDiverseString(1, 1, 7) == "ccaccbcc")
print(s.longestDiverseString(7, 1, 0) == "aabaa")