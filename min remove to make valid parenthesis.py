class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        invalid = []
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    invalid.append(i)
        # print(stack)

        for i in range(len(stack)):
            invalid.append(stack[i])

        res = ""
        for i in range(n):
            if i in invalid:
                continue
            else:
                res += s[i]

        return res
