"""
平面中有n个点，任意选出三个点p1、p2、p3，组成一个元组（p1，p2，p3），其中p1到p2的距离与p1到p3的距离相同
计算一共能找到多少这样的元组？
"""

def numberOfBoomerangs(points):
    """
    时间复杂度n^2
    空间复杂度n
    对每一个枢纽点都开辟了一个查找表，但是处理完该枢纽点时，空间就被释放了
    另外，有一个陷阱是：要注意处理点之间的距离溢出的问题，这个时候，需要使用long long来声明距离（c++中）
    :type points: List[List[int]]
    :rtype: int
    """
    solutions = 0
    for i in points:
        record = {}
        for j in points:
            if i != j:
                dist = dis(i, j)
                if dist not in record.keys():
                    record[dist] = 1
                else:
                    record[dist] += 1

        for k, v in record.items():
            solutions += v * (v - 1)  # 如果出现一次，则乘积为0，solution不受影响，不用单独判断v的长度
    return solutions


def dis(i, j):
    """
    由于两个点的距离可能不是整数，这里计算距离时，不开根号
    :param i:
    :param j:
    :return:
    """
    return (j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2



points = [[0,0],[1,0],[2,0]]
print(numberOfBoomerangs(points))