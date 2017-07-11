# instead of calculating area by height*width, we can think it in a cumulative way.
# In other words, sum water amount of each bin(width=1).

# Search from left to right and maintain a max height of left and right separately,
# which is like a one-side wall of partial container.
# Fix the higher one and flow water from the lower part.
# For example, if current height of left is lower, we fill water in the left bin.
# Until left meets right, we filled the whole container.

# Source: https://discuss.leetcode.com/topic/18720/8-lines-c-c-java-python-solution/6

def trap(height):
    n = len(height)
    l, r, water, minHeight = 0, n - 1, 0, 0
    while l < r:
        while l < r and height[l] <= minHeight:  # l < r ensures index within range
            water += minHeight - height[l]
            l += 1
        while l < r and height[r] <= minHeight:
            water += minHeight - height[r]
            r -= 1
        minHeight = min(height[l], height[r])
    return water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
