class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * word)
            else:
                stack.append(s[i])
        return ''.join(stack)
