class Solution:
    def ngr(self, nums):
        n = len(nums)
        i = n - 1
        stack = []
        res = []
        while i >= 0:
            if not stack:
                res.append(n)
            if stack and stack[-1][1] > nums[i]:
                res.append(stack[-1][0])
            if stack and stack[-1][1] <= nums[i]:
                stack.pop()
                while stack and stack[-1][1] <= nums[i]:
                    stack.pop()
                if not stack:
                    res.append(n)
                if stack and stack[-1][1] > nums[i]:
                    res.append(stack[-1][0])
            stack.append((i, nums[i]))
            i -= 1
        return res[::-1]

    def ngl(self, nums):
        n = len(nums)
        stack = []
        res = []
        for i in range(n):
            if not stack:
                res.append(-1)
            if stack and stack[-1][1] > nums[i]:
                res.append(stack[-1][0])
            if stack and stack[-1][1] <= nums[i]:
                stack.pop()
                while stack and stack[-1][1] <= nums[i]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                if stack and stack[-1][1] > nums[i]:
                    res.append(stack[-1][0])
            stack.append((i, nums[i]))
        return res

    def nsr(self, nums):
        n = len(nums)
        i = n - 1
        stack = []
        res = []
        while i >= 0:
            if not stack:
                res.append(n)
            if stack and stack[-1][1] < nums[i]:
                res.append(stack[-1][0])
            if stack and stack[-1][1] >= nums[i]:
                stack.pop()
                while stack and stack[-1][1] >= nums[i]:
                    stack.pop()
                if not stack:
                    res.append(n)
                if stack and stack[-1][1] < nums[i]:
                    res.append(stack[-1][0])
            stack.append((i, nums[i]))
            i -= 1
        return res[::-1]

    def nsl(self, nums):
        n = len(nums)
        stack = []
        res = []
        for i in range(n):
            if not stack:
                res.append(-1)
            if stack and stack[-1][1] < nums[i]:
                res.append(stack[-1][0])
            if stack and stack[-1][1] >= nums[i]:
                stack.pop()
                while stack and stack[-1][1] >= nums[i]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                if stack and stack[-1][1] < nums[i]:
                    res.append(stack[-1][0])
            stack.append((i, nums[i]))
        return res

    def solve(self, nums):
        n = len(nums)
        ngl = self.ngl(nums)
        ngr = self.ngr(nums)
        nsl = self.nsl(nums)
        nsr = self.nsr(nums)
        # print(ngl, ngr, nsl, nsr)
        ans = 0
        for i in range(n):
            gl = i - ngl[i]
            gr = ngr[i] - i
            sl = i - nsl[i]
            sr = nsr[i] - i
            print(gl, gr, sl, sr)
            ans += (gl * gr - sl * sr) * nums[i]
        return ans
