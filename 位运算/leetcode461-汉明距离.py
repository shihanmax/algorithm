# 求两个数字的二进制形式的汉明距离

"""
// c++
class Solution {
public:
    int hammingDistance(int x, int y) {
        int r = x ^ y;
        int count = 0;

        while (r) {
            count += r & 1;
            r >>= 1;
        }

        return count;
    }
};
"""