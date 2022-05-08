def nsr_index(arr):
    result, stack_ele, stack_index = [], [], []
    temp_right = len(arr)
    i = len(arr) - 1
    while i >= 0:
        if len(stack_ele) == 0:
            result.append(temp_right)
        elif len(stack_ele) > 0 and stack_ele[-1] < arr[i]:
            result.append(stack_index[-1])
        elif len(stack_ele) > 0 and stack_ele[-1] >= arr[i]:
            stack_ele.pop()
            stack_index.pop()
            while len(stack_ele) > 0 and stack_ele[-1] >= arr[i]:
                stack_ele.pop()
                stack_index.pop()
            if len(stack_ele) == 0:
                result.append(temp_right)
            elif len(stack_ele) > 0 and stack_ele[-1] < arr[i]:
                result.append(stack_index[-1])
        stack_ele.append(arr[i])
        stack_index.append(i)
        i = i-1
    return result[::-1]


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


def max_area(arr):
    ans = 0
    result = []
    v1, v2 = nsr_index(arr), nsl_index(arr)
    for i in range(len(arr)):
        d = v1[i] - v2[i]
        d = d-1
        result.append(d)

    for i, val in enumerate(arr):
        temp = result[i] * val
        ans = max(ans, temp)
    return ans


if __name__ == '__main__':
    arr = [6, 2, 5, 4, 5, 1, 6]
    print(max_area(arr))
