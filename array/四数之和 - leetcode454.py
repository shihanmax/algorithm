
"""
在四个数组中分别选出一个数，使这四个数的和为0，求这样的组合一共有多少种可能
如果暴力解的话，复杂度是n^4
本解答使用n^2的空间复杂度（使用了一个查找表），使得时间复杂度降低到n^2

当然，也可以将A和B的和的所有情况放在一个查找表中，将C和D的和的所有情况放入另一个查找表中，
然后分别遍历这两个查找表，复杂度与上述解法是一样的
"""

def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int  只需要返回一共有多少种可能即可
    数组的数据规模N为500，一个n^2的算法可以接受
    """
    record_cd = {}
    for i in C:
        for j in D:
            if i + j not in record_cd.keys():
                record_cd[i + j] = 1
            else:
                record_cd[i + j] += 1

    solutions = 0
    for i in A:
        for j in B:
            complement = 0 - (i + j)
            if complement in record_cd.keys():
                solutions += record_cd[complement]

    return solutions


A = [-1,-1]
B = [-1,1]
C = [-1,1]
D = [1,-1]

print(fourSumCount(A, B, C, D))