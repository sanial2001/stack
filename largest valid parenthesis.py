class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, stack, s = 0, [0], ')' + s
        for i in range(1, len(s)):
            if s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack.append(i)
        return ans
