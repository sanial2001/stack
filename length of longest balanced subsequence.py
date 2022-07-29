class Solution:
    def solve(self, s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                    continue
                stack.append(i)
        # print(stack)
        return len(s) - len(stack)
