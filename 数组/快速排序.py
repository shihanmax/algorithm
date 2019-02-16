
def partation(arr, l, r):
    pivot = r
    while l < r:
        while arr[l] <= arr[pivot] and l < r:
            l += 1
        while arr[r] >= arr[pivot] and l < r:
            r -= 1

        if arr[l] != arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
    arr[l], arr[pivot] = arr[pivot], arr[l]
    return l

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