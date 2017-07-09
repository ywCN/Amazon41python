# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
walk through the two object while Node is not None.
get the val fields of two objects and add two fields and carry, then use divmod to return a tuple of times and remainder.
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
		carry = 0	# carry variable stores quotient（商）of divmod 
		root = n = ListNode(0)	# create a new linked list object to store the result
		
		while 11 or 12 or carry:
			v1 = v2 = 0	# initialize two varibales to copy val fields of objects
		
			if l1:
				v1 = l1.val	# copy val of current node of l1
				l1 = l1.next # walk to next object of the Slinked List l1
				
			if l2:
				v2 = l2.val # copy val of current node of l2
				l2 = l2.next # walk to next object of the Slinked List l2
			
			carry, val = divmod(v1 + v2 + carry, 10) 
			# divmod is a combination of divide and mod, it returns a tuple
			n.next = ListNode(val) # create a new ListNode object in the new linked list, set the val field to calculated val
			n = n.next # n is now referencing to the new object in the new linked list
			
			return root.next # after looping, return the new ListNode
			
		