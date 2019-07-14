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


def is_rotated_string(str_a, str_b):
    if len(str_a) != len(str_b):
        return False

    if str_a == str_b:
        return True

    dump_str_a = str_a + str_a

    return dump_str_a.find(str_b) is not None


str_a = 'abcde'
str_b = 'cdeab'

print(is_rotated_string(str_a, str_b))