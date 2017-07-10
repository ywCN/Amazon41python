#  Since it's 3 sum, there's only going to be 3 numbers
#  Iterate through the list with the first pointer, and then trying to find two extra numbers to sum to 0.
#  Since the list is ordered, the right pointer will always be higher than the left pointer.

#  So if the sum is too large, you can move the right pointer back one.
#  On the other hand, if the sum is too small (below 0), then move the left pointer up one.

#  Source: https://discuss.leetcode.com/topic/22619/python-easy-to-understand-solution-o-n-n-time/23

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

        l = i + 1  # left pointer
        r = len(nums) - 1  # right pointer

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
