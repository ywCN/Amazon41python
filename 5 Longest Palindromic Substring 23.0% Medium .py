# O(n^2)

# This is a slow solution because it does some duplicated work in the string. However, it is easy to understand.

# This program will loop through the string from left to right,
# trying to check if an element can expand to a larger palindrome substring,
# and returns the longest substring

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """

    res = ""
    for i in range(len(s)):

        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp

        # even case, like "abba"
        tmp = helper(s, i, i + 1)
        if len(tmp) > len(res):
            res = tmp

    return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer

def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1  # expand to left
        r += 1  # expand to right
    return s[l + 1:r]

'''
x = longestPalindrome('FGGFFadfsssfbd')
print(x)
'''