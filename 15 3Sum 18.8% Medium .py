def threeSum(nums):
    """
    type nums: List[int]
    rtype: List[List[int]]
    """

    nums = sorted(nums)
    result = []

    for i in range(len(nums) - 2):
        # -2 because the result must be a 3 elements list
        if i > 0 and nums[i] == nums[i - 1]:  # because the answers should be unique
            continue

        l = i + 1
        r = len(nums) - 1

        while r > l:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return result



x = threeSum([-1, 0, 1, 2, -1, -4])
print(x)
