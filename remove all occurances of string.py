class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ''
        for i in s:
            res = res + i
            while len(res) >= len(part):
                # print(res)
                index = len(res) - len(part)
                if res[index:] == part:
                    temp = res[:index]
                    res = temp
                else:
                    break
        return res
