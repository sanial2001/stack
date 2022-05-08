def solve(arr):
    n = len(arr)
    maxL = [None] * len(arr)
    maxR = [None] * len(arr)
    maxL[0], maxR[n-1] = arr[0], arr[n-1]
    for i in range(1, n):
        maxL[i] = max(maxL[i-1], arr[i])
    for i in range(n-2, -1, -1):
        maxR[i] = max(maxR[i+1], arr[i])

    min_arr = []
    for i in range(n):
        min_arr.append(min(maxL[i], maxR[i]))

    result = []
    for i in range(n):
        result.append(min_arr[i] - arr[i])

    sum_water = 0
    for i in range(n):
        sum_water = sum_water + result[i]

    return sum_water


if __name__ == '__main__':
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(solve(arr))
