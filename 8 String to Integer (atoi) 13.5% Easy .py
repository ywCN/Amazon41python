# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found.

# Then, starting from this character,
# takes an optional initial plus or minus sign followed by as many numerical digits as possible,
# and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.


def myAtoi(s):
    """
    :type str: str
    :rtype: int
    """

    s = s.strip()

    if len(s) == 0:
        return 0

    tmp = '0'
    result = 0
    i = 0  # stores the current index of the string s

    if s[0] in '-+':
        tmp = s[0]
        i = 1

    MAX_INT = 2147483647
    MIN_INT = -2147483648

    for i in range(i, len(s)):

        if s[i].isdigit():
            tmp += s[i]
        else:
            break

        if len(tmp) > len(MAX_INT) - 1:
            result = int(tmp)

        if result > MAX_INT:
            return MAX_INT

        elif result < MIN_INT:
            return MIN_INT

        else:
            return result

