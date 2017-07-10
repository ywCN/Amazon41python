#  https://discuss.leetcode.com/topic/11783/one-line-python-solution/22

def letterCombinations(digits):
    if digits == '':  # special case
        return []
    letter_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = ['']
    for digit in digits:
        tmp = []  # store result for this digit in this loop
        for y in res:  # loop each element in current result
            for x in letter_map[digit]:  # loop each element for the letters of current number
                tmp.append(y + x)
        res = tmp

    return res

