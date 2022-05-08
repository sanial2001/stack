class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ")":
                temp = ""
                while stack and stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                for ch in temp:
                    stack.append(ch)
            else:
                stack.append(s[i])

        res = ""
        for word in stack:
            res += word
        return res
