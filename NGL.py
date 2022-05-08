def ngl(arr):
    stack = []
    result = []
    n = len(arr)
    for i in range(n):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            result.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            elif len(stack) > 0 and stack[-1] > arr[i]:
                result.append(stack[-1])
        stack.append(arr[i])
    return result


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    print(ngl(arr))
