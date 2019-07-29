"""
给定一个整形数组和一个数字s，找到数组中最短的一个连续子数组，使得连续子数组的和
sum大于等于s，返回这个连续子数组的长度
"""
def minSubArrayLen(arr, s):
    left = 0
    right = -1
    sum = 0
    res = len(arr) + 1

    while left < len(arr):
        if right+1 < len(arr) and sum < s:
            sum += arr[right]
            right += 1
        else:
            sum -= arr[left]
            left += 1

        if sum >= s:
            res = min(res, right-left+1)

    if res == len(arr) + 1:
        return 0

    return res


arr = [2, 3, 1, 2, 4, 3]

print(minSubArrayLen(arr, 7))

