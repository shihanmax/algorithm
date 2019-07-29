
def partation(arr, l, r):
    pivot = r  # 取最右侧为pivot
    while l < r:
        while arr[l] <= arr[pivot] and l < r:
            l += 1
        while arr[r] >= arr[pivot] and l < r:
            r -= 1

        if arr[l] != arr[r]:  # 不相等时才进行交换，避免死循环
            arr[l], arr[r] = arr[r], arr[l]

    arr[r], arr[pivot] = arr[pivot], arr[r]  # 将pivot与最右侧做交换

    return r


def _quickSort(arr, l, r):
    pivot = partation(arr, l, r)
    if pivot > l:
        _quickSort(arr, l, pivot-1)
    if pivot < r:
        _quickSort(arr, pivot+1, r)


def quickSort(arr):
    _quickSort(arr, 0, len(arr)-1)


arr = [1, 23, 78, 6, -5, 78, 3, 3]

print(arr)
quickSort(arr)
print(arr)