class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        while popped:
            if stack and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()
            elif pushed:
                stack.append(pushed.pop(0))
            else:
                return False

        return True
