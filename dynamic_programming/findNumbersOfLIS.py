def findNumbersOfLIS(arr):
    n = len(arr)
    max_len = 1
    res = 0

    dp = [1] * n
    cnt = [1] * n
    
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                cnt[i] = cnt[j]
            elif arr[j] < arr[i] and dp[j] + 1 == dp[i]:
                cnt[i] += cnt[j]
        
        max_len = max(max_len, dp[i])

    for i in range(n):
        if dp[i] == max_len:
            res += cnt[i]
    return res

print(findNumbersOfLIS([1, 3, 5, 4, 7]))
print(findNumbersOfLIS([2,2,2,2,2]))

