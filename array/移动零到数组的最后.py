"""
将一个数组中所有的0移动到数组的最后
[1, 0, 2, 5, 0, 7] -> [1, 2, 5, 7, 0, 0]
"""

def moveZeros(arr):
    curr = 0
    length = len(arr)
    for i in range(length):
        if arr[i] != 0:
            arr[curr] = arr[i]
            curr += 1
    for i in range(curr, length):
        arr[i] = 0


arr = [1, 0, 2, 5, 0, 7]
print(arr)
moveZeros(arr)
print(arr)