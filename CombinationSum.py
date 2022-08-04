# BackTracking Solution
def combinationSum(num,target):
    output = []
    subset = []
    cur = 0
    def backTracking(i,total,subset):
        if cur == target:
            output.append(subset.copy())
            return
        if i > len(num) - 1 or target < 0:
            return
        subset.append(num[i])
        backTracking(i,target - num[i],subset.copy())
        subset.pop()

        subset.append(num[i+1])
        backTracking(i+1,target - num[i+1],subset.copy())
        return
    backTracking(0,7,[])
    return output
print(combinationSum([2,3,6,7],7))


#
# # BackTracking Solution
# def combinationSum(candidates,target):
#     res = []
#
#     def backTracking(i,cur,total):
#         if total == target:
#             res.append(cur.copy())
#             return
#         if i>= len(candidates) or total > target:
#             return
#         cur.append(candidates[i])
#         backTracking(i,cur,total + candidates[i])
#         cur.pop()
#         backTracking(i+1,cur,total)
#
#     backTracking(0,[],0)
#     return res
#     print(combinationSum([2,3,6,7],7))

