class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if sorted(list(set(nums)), reverse=True) == nums and nums[0]!=nums[-1]:
            res = [nums[0] for _ in range(len(nums))]
            res[0] = -1
            return res
        stack, res = [], []
        i = len(nums)-1
        while i >= 0:
            stack = nums[i+1:] + nums[:i]
            #print(stack)
            if len(stack) > 0 and stack[0] > nums[i]:
                res.append(stack[0])
            elif len(stack) > 0 and stack[0] <= nums[i]:
                stack.pop(0)
                while len(stack) > 0 and stack[0] <= nums[i]:
                    stack.pop(0)
                if len(stack) == 0:
                    res.append(-1)
                elif len(stack) > 0 and stack[0] > nums[i]:
                    res.append(stack[0])
            i = i-1
        return res[::-1] if res else [-1]