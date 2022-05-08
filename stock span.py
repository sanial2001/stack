def stock_span(arr, target):
    stack, result, stock = [], [], []
    n = len(arr)
    for i in range(n):
        if len(stack) == 0:
            result.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            result.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            stock.append(stack.pop())
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stock.append(stack.pop())
            if len(stack) == 0:
                result.append(-1)
            elif len(stack) > 0 and stack[-1] > arr[i]:
                result.append(stack[-1])
        if arr[i] == target:
            stock.append(arr[i])
            break
        stack.append(arr[i])
    return stock


if __name__ == '__main__':
    arr = [100, 80, 60, 70, 60, 75, 85]
    print(stock_span(arr, 85))
