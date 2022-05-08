class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        temp, res = "", ""
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")":
                stack.pop()
            if len(stack) > 1 or (stack and s[i] == ")"):
                temp += s[i]
            if len(stack) == 0:
                res += temp
                temp = ""

        return res
