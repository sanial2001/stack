class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = []
        n = len(nums)
        for i, num in enumerate(nums):
            while stack and num < stack[-1] and (len(stack)-1) + (n-i) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack