class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = temperatures[:]
        stack, res, index = [], [], []
        i = len(arr) - 1

        while i >= 0:
            if len(stack) == 0:
                res.append(0)
            elif len(stack) > 0 and stack[-1] > arr[i]:
                res.append(index[-1] - i)
            else:
                stack.pop()
                index.pop()
                while len(stack) > 0 and stack[-1] <= arr[i]:
                    stack.pop()
                    index.pop()
                if len(stack) == 0:
                    res.append(0)
                else:
                    res.append(index[-1] - i)
            stack.append(arr[i])
            index.append(i)
            i = i - 1

        return res[::-1]