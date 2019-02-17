'''
两个长度均小于5100的字符串，均是规范的数字，它们不以0为开头，只包含0～9
将这两个字符串代表的数字相加，返回字符串形式的结果
'''

"""
//c++

class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() - 1;
        int j = num2.size() - 1;
        
        int carry = 0;
        string result = "";
            
        while (i >= 0 || j >= 0) {
            if (i >= 0) {
                carry += (num1[i] - '0');
            }
            if (j >= 0) {
                carry += (num2[j] - '0');
            }
            result += (char) (carry % 10 + '0');
            carry /= 10;
            i--;
            j--;
        }
        
        if (carry == 1) {
            result += '1';
        }
        
        reverse(result.rbegin(),result.rend());
        
        return result;
    }
};

"""