
def partation(arr, left, right):
    pivot = right
    while left < right:
        while arr[left] <= arr[pivot] and left < right:
            left += 1
        while arr[right] >= arr[pivot] and left < right:
            right -= 1

        if arr[left] != arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
    arr[right], arr[pivot] = arr[pivot], arr[right]
    return right
 

def _findKthLarge(arr, left, right, k):
    assert k >= 1 and k <= len(arr)

    length = len(arr)
    pivot = partation(arr, left, right)
    if k == length - pivot:
        return arr[pivot]
    elif k > length - pivot:
        return _findKthLarge(arr, left, pivot - 1, k)
    else:
        return _findKthLarge(arr, pivot + 1, right, k)


def findKthLarge(arr, k):
    return _findKthLarge(arr, 0, len(arr) - 1, k)


arr = [1, 23, 77, 6, -5, 78, 3, 3]
print(findKthLarge(arr, 3))