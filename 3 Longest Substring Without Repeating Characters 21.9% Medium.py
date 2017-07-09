#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
		used_char = {} # key: char in s		value: index of char in s
		max_length = start = 0
		
		for i, c in enumerate(s):
			if c in used_char and start <= used_char[c]:
				start = used_char[c] + 1
			else:
				max_length = max(max_length, i - start + 1)
			
			used_char[c] = i
			
		return max_length
