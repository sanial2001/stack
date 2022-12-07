# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        n = len(s)
        i, stack = 0, []

        while i < n:
            depth, val = 0, ''
            while i < n and s[i] == '-':
                depth, i = depth + 1, i + 1
            while i < n and s[i] != '-':
                val, i = val + s[i], i + 1
            while stack and len(stack) > depth:
                stack.pop()
            node = TreeNode(int(val))
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]