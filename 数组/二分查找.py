"""
使用二分查找法，在给定有序数组中查找指定元素
"""

def binSearch(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1




# 二分查找拓展：寻找有序数组中第一个与num相等的数
def findFirstEq(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if num > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if left < len(arr)-1 and arr[left] == num:
        return left
    return -1


# 二分查找拓展：寻找有序数组中最后一个与num相等的数
def findLastEq(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if num >= arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if right > 0 and arr[right] == num:
        return right
    return -1


arr = [1, 1, 3, 5, 7, 14, 14, 14, 25, 36, 47, 66, 90, 90]

print(binSearch(arr, 14))
print(findFirstEq(arr, 14))
print(findLastEq(arr, 14))

