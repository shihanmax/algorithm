"""
在数组中寻找两个数字，这两个数字的和为target

暴力法：O(n^2)
常规法：O(nlogn)
此法：O(n) + O(n)空间
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    record = {}  # 查找表

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in record.keys():
            return [i, record[complement]]
        else:
            record[nums[i]] = i

    raise Exception('invalid input')


nums = [2, 7, 9, 16]
target = 9

print(twoSum(nums, target))