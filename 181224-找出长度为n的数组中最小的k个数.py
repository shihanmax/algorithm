# 在长度为n的数组中找出最小/大的k个数

def partition(arr, start, end):
    if end <= start:
        return
    base = arr[start]
    index1, index2 = start, end
    while start < end:
        while start < end and arr[end] >= base:
            end -= 1
        arr[start] = arr[end]
        
        while start < end and arr[start] <= base:
            start += 1
        arr[end] = arr[start]
    arr[start] = base
    partition(arr, index1, start - 1)
    partition(arr, start + 1, index2)

def find_least_k_nums(arr, k):
    length = len(arr)
    if not arr or k <= 0 or k > length:
        return None
    start = 0
    end = length - 1
    partition(arr, start, end)
    return arr[:k]
    
arr = [1, 23, 58, 2, 66, 9]

print(find_least_k_nums(arr, 3))