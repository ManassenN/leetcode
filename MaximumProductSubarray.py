
def maxProduct(nums):
    res = max(nums)
    curMin,curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin,curMax = 1, 1
            continue

        tmp = curMax  * n
        curMax= max(tmp,n * curMin , n)
        curMin = min(tmp, n * curMin, n)
        res = max(curMax,res)

    return res


print(maxProduct([-4,-3,-2]))