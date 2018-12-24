
def find_max_sub_arr(arr):
    """
    使用两个变量分别记录目前的子数组和和当前最大的子数组和
    当目前的子数组和小于0时，舍弃它
    否则，如果当前子数组和大于当前最大子数组和，更新之
    """
    whole_sum = arr[0]
    current_sum = 0
    
    for i in arr:
        if current_sum < 0:
            current_sum = i
        else:
            current_sum += i
        if current_sum > whole_sum:
            whole_sum = current_sum
            
    return whole_sum

    
if __name__ == '__main__':
    array = [0, -6, 3, 5, -1, 2]
    find_max_sub_arr(a)
