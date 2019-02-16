

"""
给定一个数组nums，给定一个窗口大小k，判断nums数组中，在长度为k的窗口内是否存在相等的元素
如[1, 2, 3, 1]中，如果窗口为2，则不存在，返回False
如果窗口为3，则存在，返回True，因为两个元素1的下标的差为3-0 = 3
"""

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    暴力解法：nk
    时间复杂度：n
    空间复杂度：k
    """
    record = set()
    for i in range(len(nums)):
        if nums[i] in record:
            return True
        else:
            record.add(nums[i])

        if len(record) == k+ 1:
            record.remove(nums[i - k])  # 如果k等于3，那么遍历到第四个元素时，就应该把第3-3=0个元素删除
    return False


nums = [1,2,3,1]
k = 2

print(containsNearbyDuplicate(nums, k))