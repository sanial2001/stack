class Solution:
    def minSwaps(self, s: str) -> int:
        mx_cnt, cnt = 0, 0
        for i in range(len(s)):
            if s[i] == "]":
                cnt += 1
                mx_cnt = max(mx_cnt, cnt)
            else:
                cnt -= 1
        return (mx_cnt + 1) // 2
