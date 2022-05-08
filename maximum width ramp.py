class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                idx = stack.pop()
                ans = max(ans, i-idx)
        return ans