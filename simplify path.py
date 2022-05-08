class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for curr in path:
            if curr == "" or curr == ".":
                continue
            elif curr == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(curr)

        res = ""
        for curr in stack:
            res = res + "/" + curr

        return "/" if len(res) == 0 else res
