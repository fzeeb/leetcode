"""
Given a list of words, list of  single letters (might be repeating) and score of every character.
Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.

Example 2:
Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
Output: 27
Explanation:
Score  a=4, b=4, c=4, x=5, z=10
Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
Word "xxxz" only get a score of 25.

Example 3:
Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
Output: 0
Explanation:
Letter "e" can only be used once.

Constraints:
    1 <= words.length <= 14
    1 <= words[i].length <= 15
    1 <= letters.length <= 100
    letters[i].length == 1
    score.length == 26
    0 <= score[i] <= 10
    words[i], letters[i] contains only lower case English letters.

Hint 1
Note that words.length is small. This means you can iterate over every subset of words (2^N).
"""
from typing import List
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # Step 1: Convert letters list into a frequency count
        letter_count = [0] * 26
        for letter in letters:
            letter_count[ord(letter) - ord('a')] += 1
        
        # Step 2: Pre-calculate scores for each word
        word_scores = []
        word_letter_counts = []
        for word in words:
            curr_score = 0
            curr_letter_count = [0] * 26
            for char in word:
                index = ord(char) - ord('a')
                curr_score += score[index]
                curr_letter_count[index] += 1
            word_scores.append(curr_score)
            word_letter_counts.append(curr_letter_count)
        
        # Step 3: Iterate over all subsets of words using bitmasking
        max_score = 0
        num_words = len(words)
        for subset in range(1 << num_words):
            subset_score = 0
            used_letters = [0] * 26
            valid = True
            
            for i in range(num_words):
                if subset & (1 << i):
                    # Add this word's score if it can be used with available letters
                    for j in range(26):
                        used_letters[j] += word_letter_counts[i][j]
                        if used_letters[j] > letter_count[j]:
                            valid = False
                            break
                    if not valid:
                        break
                    subset_score += word_scores[i]
            
            if valid:
                max_score = max(max_score, subset_score)
        
        return max_score
    
print (Solution().maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])) # 23
print (Solution().maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])) # 27
print (Solution().maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])) # 0
                                                                                    