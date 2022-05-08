def ngr(arr):
    stack = []
    result = []
    i = len(arr) - 1
    while i >= 0:
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            result.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()
            while stack[-1] <= arr[i] and len(stack) > 0:
                stack.pop()
            if len(stack) == 0:
                result.append(-1)
            elif len(stack) > 0 and stack[-1] > arr[i]:
                result.append(stack[-1])
        stack.append(arr[i])
        i = i - 1
    return result[::-1]


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    print(ngr(arr))
