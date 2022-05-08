def nsl_index(arr):
    result, stack_ele, stack_index = [], [], []
    for i in range(len(arr)):
        if len(stack_ele) == 0:
            result.append(-1)
        elif len(stack_ele) > 0 and stack_ele[-1] < arr[i]:
            result.append(stack_index[-1])
        elif len(stack_ele) > 0 and stack_ele[-1] >= arr[i]:
            stack_ele.pop()
            stack_index.pop()
            while len(stack_ele) > 0 and stack_ele[-1] >= arr[i]:
                stack_ele.pop()
                stack_index.pop()
            if len(stack_ele) == 0:
                result.append(-1)
            elif len(stack_ele) > 0 and stack_ele[-1] < arr[i]:
                result.append(stack_index[-1])
        stack_ele.append(arr[i])
        stack_index.append(i)
    return result


if __name__ == '__main__':
    arr = [4, 5, 2, 10, 8]
    print(nsl_index(arr))
