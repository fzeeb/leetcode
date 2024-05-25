"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
    Input is generated in a way that the length of the answer doesn't exceed 10^5.
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Step 1: Convert wordDict into a set for faster lookups
        word_set = set(wordDict)
        
        # Step 2: Create a memoization table to store the possible sentences for each index
        memo = {}
        
        # Step 3: Create a recursive function to find the possible sentences for each index
        def wordBreakHelper(index):
            # Base case: If the index is already in the memo table, return the value
            if index in memo:
                return memo[index]
            
            # Base case: If the index is the length of the string, return an empty list
            if index == len(s):
                return [""]
            
            # Recursive case: Find the possible sentences for the rest of the string
            result = []
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in word_set:
                    sentences = wordBreakHelper(i)
                    for sentence in sentences:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)
            
            # Store the result in the memo table and return it
            memo[index] = result
            return result
        
        # Step 4: Call the recursive function starting from index 0
        return wordBreakHelper(0)
        
print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])) # ["cats and dog","cat sand dog"]
print(Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"])) # ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # []