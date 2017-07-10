# https://discuss.leetcode.com/topic/6534/simple-python-solution-with-stack

#  Solution 1
"""
def isValid(s):

	#  type s: str
	#  rtype: bool

    stack = []
    dict = {']': '[', ')': '(', '}': '{'}

    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False

    return stack == []

"""


# Solution 2

def isValid(s):

	#  type s: str
	#  rtype: bool

    n = len(s)
    if n == 0:
        return True

    if n % 2 != 0:
        return False

    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('{}', '').replace('()', '').replace('[]', '')

    if s == '':
        return True
    else:
        return False


print(isValid("{([])}"))
print(isValid("([)]"))
