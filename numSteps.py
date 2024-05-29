"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
    If the current number is even, you have to divide it by 2.
    If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0

Constraints:
    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'

Hint 1
Read the string from right to left, if the string ends in '0' then the number is even otherwise it is odd.

Hint 2
Simulate the steps described in the binary string.
"""
class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        steps = 0
        carry = 0
        for i in range(n-1, 0, -1):
            if s[i] == '0':
                if carry == 0:
                    steps += 1
                else:
                    steps += 2
            else:
                if carry == 0:
                    steps += 2
                    carry = 1
                else:
                    steps += 1
        if carry == 1:
            steps += 1
        return steps

print (Solution().numSteps("1101")) # 6
print (Solution().numSteps("10")) # 1
print (Solution().numSteps("1")) # 0