'''
http://bookshadow.com/weblog/2015/04/05/leetcode-longest-substring-without-repeating-characters/

“Sliding Window Algorithm”

start and end store the substring's start and end
countDict store the current number of chars 

loop through the string and increase end by 1 in each loop

whenever the the current number of chars is greater than 1, decrease the number of s[start] in the dict and increase start by 1 until countDict[c] is not greater than 1
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

		max_len, start, end = 0, 0, 0
		countDict = {} # key: char		value: number of chars

		for c in s:
			end += 1
			countDict[c] = countDict.get(c, 0) + 1
			while countDict[c] > 1: 
			# decrease the value in the dict begins from s[start] and increase start by 1 until the value of s[start] is not bigger than 1
				countDict[s[start]] -= 1
				start += 1

			max_len = max(max_len, end - start)

		return max_len
