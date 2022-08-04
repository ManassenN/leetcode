
def permute(nums):
    results = []

    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)


        for perm in perms:
            perm.append(n)

        results.extend(perms)
        nums.append(n)
    return results

print(permute([1,2,3,4]))