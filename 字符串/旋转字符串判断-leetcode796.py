# 判读两个字符串是否互为旋转字符串
# 如abcde和cdeab是旋转字符串

"""
//c++

class Solution {
public:
    bool rotateString(string A, string B) {
        if (A.size() != B.size())
            return false;
        if (A == B)
            return true;

        A += A;
        return A.find(B) != string::npos;
    }
};
"""