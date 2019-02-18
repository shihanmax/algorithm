"""
计算逆波兰表达式
//C++

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        //计算逆波兰表达式
        if (tokens.size() == 1) {
            return stoi(tokens[0]);
        }

        stack<int> s;

        for (int i=0; i< tokens.size(); i++) {
            if (tokens[i] != "+" && tokens[i] != "-" && tokens[i] != "*" && tokens[i] != "/") {
                int num = stoi(tokens[i]);
                s.push(num);
            } else {
                int op_num1 = s.top();s.pop();
                int op_num2 = s.top();s.pop();
                if (tokens[i] == "+") s.push(op_num2 + op_num1);
                else if (tokens[i] == "-") s.push(op_num2 - op_num1);
                else if (tokens[i] == "*") s.push(op_num2 * op_num1);
                else s.push(op_num2 / op_num1);
            }
        }
        return s.top();
    }
};

"""