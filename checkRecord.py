"""
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:ß
    'A': Absent.
    'L': Late.
    'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:
    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 10^9 + 7.

Example 1:
Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:
Input: n = 1
Output: 3

Example 3:
Input: n = 10101
Output: 183236316

Constraints:
    1 <= n <= 10^5
"""
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j][k] means the number of valid sequences of length i with j 'A's and ending with k 'L's
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        
        # Base case: Length 0, one empty sequence
        dp[0][0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P'
                    dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][k]) % MOD
                    # Add 'L'
                    if k < 2:
                        dp[i][j][k+1] = (dp[i][j][k+1] + dp[i-1][j][k]) % MOD
                    # Add 'A'
                    if j < 1:
                        dp[i][j+1][0] = (dp[i][j+1][0] + dp[i-1][j][k]) % MOD
        
        # Sum all valid sequences of length n
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        
        return result
        
print (Solution().checkRecord(2)) # 8
print (Solution().checkRecord(1)) # 3
print (Solution().checkRecord(10101)) # 183236316