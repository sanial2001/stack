class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = []
        dom = list(dominoes)
        n = len(dom)

        for i, pos in enumerate(dom):
            if pos == "L" or pos == "R":
                q.append((i, pos))

        while q:
            i, pos = q.pop(0)
            if pos == "L":
                if i > 0 and dom[i - 1] == ".":
                    dom[i - 1] = "L"
                    q.append((i - 1, "L"))

            elif pos == "R":
                if i + 1 < n and dom[i + 1] == ".":
                    if i + 2 < n and dom[i + 2] == "L":
                        q.pop(0)
                    else:
                        dom[i + 1] = "R"
                        q.append((i + 1, "R"))

        return "".join(dom)
