#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
		ans, start, end = 0, 0, 0
		countDict = {}
		
		for c in s:
			end += 1
			countDict[c] = countDict.get(c, 0) + 1
