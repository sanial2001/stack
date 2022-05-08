def nsr_index(arr):
    result, stack_ele, stack_index = [], [], []
    i = len(arr) - 1
    temp_right = len(arr)
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
        i = i - 1
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
    width = []
    ans = 0
    v1, v2 = nsr_index(arr), nsl_index(arr)
    for i in range(len(arr)):
        d = v1[i] - v2[i] - 1
        width.append(d)

    for i, val in enumerate(arr):
        temp = val * width[i]
        ans = max(temp, ans)
    return ans


def max_binary(matrix):
    n = len(matrix[0])
    t = matrix[0]
    max_val = max_area(t)
    for i in range(1, n):
        for j in range(n):
            if matrix[i][j] == 0:
                t[j] = 0
            else:
                t[j] = t[j] + matrix[i][j]
        val = max_area(t)
        max_val = max(max_val, val)
    return max_val


if __name__ == '__main__':
    matrix = [[0, 1, 1, 0],
              [1, 1, 1, 1],
              [1, 1, 1, 1],
              [1, 1, 0, 0]]
    print(max_binary(matrix))
