arr = [-2,1,-3,4,-1,2,1,-5,4]

import math

def maxSubArraySum(arr):
    curSum = arr[0]
    result =  - math.inf

    for num in arr[1:]:
        if curSum > 0:
            curSum += num
        else:
            curSum = num

        result = max(curSum, result)

    return result

print(maxSubArraySum(arr))