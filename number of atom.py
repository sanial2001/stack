class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        for i in range(len(formula)):
            if formula[i] == ')':
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                element = ''
                while stack[-1] != '(':
                    element = stack.pop() + element
                stack.pop()
                stack.append(int(num) * element)
            else:
                stack.append(formula[i])
        print(''.join(stack))


if __name__ == '__main__':
    Solution().countOfAtoms(formula = "Mg(OH)2")
