"""
在数组中，找到一个连续子数组，该子数组的和大于给定数字s，求子数组的最短长度

//c++

class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        // 双指针/快慢指针
        int slow = 0;
        int fast = 0;
        int sum = 0;
        int minLength = INT_MAX;

        while (fast < nums.size()) {
            sum += nums[fast++];

            while (sum >= s && slow < fast) {
                minLength = min(minLength, fast - slow);
                sum -= nums[slow++];
            }
        }
        return minLength==INT_MAX ? 0 : minLength;
    }
};
"""