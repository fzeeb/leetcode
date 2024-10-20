"""
A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
    't' that evaluates to true.
    'f' that evaluates to false.
    '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
    '&(subExpr_1, subExpr_2, ..., subExpr_n)' that evaluates to the logical AND of the inner expressions subExpr_1, subExpr_2, ..., subExpr_n where n >= 1.
    '|(subExpr_1, subExpr_2, ..., subExpr_n)' that evaluates to the logical OR of the inner expressions subExpr_1, subExpr_2, ..., subExpr_n where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.

Example 1:
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.

Constraints:
    1 <= expression.length <= 2 * 10^4
    expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

Hint 1
Write a function "parse" which calls helper functions "parse_or", "parse_and", "parse_not".
"""
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(expr: str, i: int) -> bool:
            if expr[i] == 't':
                return True, i + 1
            if expr[i] == 'f':
                return False, i + 1
            if expr[i] == '!':
                return parse_not(expr, i + 2)
            if expr[i] == '&':
                return parse_and(expr, i + 2)
            if expr[i] == '|':
                return parse_or(expr, i + 2)
        
        def parse_not(expr: str, i: int) -> bool:
            res, i = parse(expr, i)
            return not res, i + 1
        
        def parse_and(expr: str, i: int) -> bool:
            res, i = parse(expr, i)
            while expr[i] != ')':
                temp, i = parse(expr, i + 1)
                res = res and temp
            return res, i + 1
        
        def parse_or(expr: str, i: int) -> bool:
            res, i = parse(expr, i)
            while expr[i] != ')':
                temp, i = parse(expr, i + 1)
                res = res or temp
            return res, i + 1
        
        return parse(expression, 0)[0]
        

# Test Cases
s = Solution()
print(s.parseBoolExpr("&(|(f))") == False)
print(s.parseBoolExpr("|(f,f,f,t)") == True)
print(s.parseBoolExpr("!(&(f,t))") == True)