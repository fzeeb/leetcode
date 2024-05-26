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
        # Step 1: Define the modulo value
        MOD = 10**9 + 7
        
        # Step 2: Create a memoization table to store the number of possible attendance records
        memo = {}
        
        # Step 3: Create a recursive function to find the number of possible attendance records
        def checkRecordHelper(index, absent, late):
            # Base case: If the index is already in the memo table, return the value
            if (index, absent, late) in memo:
                return memo[(index, absent, late)]
            
            # Base case: If the index is the length of the string, return 1
            if index == n:
                return 1
            
            # Recursive case: Find the number of possible attendance records for the rest of the string
            result = 0
            
            # Case 1: Add a 'P' for present
            result += checkRecordHelper(index + 1, absent, 0)
            
            # Case 2: Add an 'A' for absent
            if absent < 1:
                result += checkRecordHelper(index + 1, absent + 1, 0)
            
            # Case 3: Add an 'L' for late
            if late < 2:
                result += checkRecordHelper(index + 1, absent, late + 1)
            
            # Store the result in the memo table and return it
            memo[(index, absent, late)] = result % MOD
            return memo[(index, absent, late)]
        
        # Step 4: Call the recursive function with the initial values
        return checkRecordHelper(0, 0, 0)
        
print (Solution().checkRecord(2)) # 8
print (Solution().checkRecord(1)) # 3
print (Solution().checkRecord(10101)) # 183236316