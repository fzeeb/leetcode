"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
    0 <= num <= 108
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(map(int, str(num)))
        l = len(n)
 
        for i in range (0, l - 1):
            sub = n[i:l]
            m = max(sub)
            indices = []
            for k in range(len(sub)):
                if(sub[k] == m):
                    indices.append(k)

            j = max(indices)
            if n[i] < m:
                n[j+i] = n[i]
                n[i] = m
                    
                ans = int(''.join(map(str, n)))
                return ans

        return num
    
# Test cases
s = Solution()
print(s.maximumSwap(2736) == 7236)
print(s.maximumSwap(9973) == 9973)
print(s.maximumSwap(98368) == 98863)
print(s.maximumSwap(1993) == 9913)
