class Solution:
    def maxDepth(self, s: str) -> int:
        cnt, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            ans = max(ans, cnt)
        return ans
