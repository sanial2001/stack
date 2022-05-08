class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k = k - 1
            stack.append(n)

        while stack and k:
            stack.pop()
            k = k - 1

        while stack and stack[0] == '0':
            stack.pop(0)

        return ''.join(stack) if stack else '0'
