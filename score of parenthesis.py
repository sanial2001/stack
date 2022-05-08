class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, res = [], 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                while stack and stack[-1] != "(":
                    res += stack[-1]
                    stack.pop()
                stack[-1] = 1 if res == 0 else res * 2
                res = 0
        return sum(stack)
