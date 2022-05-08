class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    ans += 1
        return ans + len(stack)
