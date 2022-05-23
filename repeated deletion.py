class Solution:
    def solve(self, s):
        stack = []
        prev = ''
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            elif prev == i:
                continue
            else:
                stack.append(i)
            prev = i
        return "".join(stack)
