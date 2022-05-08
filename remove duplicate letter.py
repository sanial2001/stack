class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        d = {char: i for i, char in enumerate(s)}

        for i, char in enumerate(s):
            if char not in stack:
                while stack and char < stack[-1] and d[stack[-1]] > i:
                    stack.pop()
                stack.append(char)

        return ''.join(stack)