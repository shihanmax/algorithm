"""
滑动窗口法
abcabcbb -> abc
bbbbb -> b
pwwkew -> wke
"""

def findLongestSubstring(s):
    freq = [0] * 256  # 存放字符的ascii码值
    left = 0
    right = -1  # 滑动窗口是[l, r]
    res = 0

    while left < len(s):
        if right + 1 < len(s) and freq[ord(s[right+1])] == 0:
            right += 1
            freq[ord(s[right])] += 1
        else:
            freq[ord(s[left])] -= 1
            left += 1
        res = max(res, right - left + 1)

    return res

s = 'abcseabcbad'
print(findLongestSubstring(s))

