# Compare the values of both lists until one list is empty, 
# then move the rest of the nodes from the other list to merged list


#  both linked list are sorted
"""
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution():
    def mergeTwoLists(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
		"""
        dummy = ListNode(0)
        tmp = dummy

        while l1 != None and l2 != None:
            # execute following lines if both lists are not at the end
            # copy bigger values to the new ListNodes until reached at least one end(None)
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next

            tmp = tmp.next  # go to next node

        if l1 != None:  # rest of the nodes must be in only one linked list, so just copy the head node of the list (just refer tmp.next to the current head node of the leftover list)
            tmp.next = l1
        else:
            tmp.next = l2

        return dummy.next  # dummy.next is the head of the returned list


"""
node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = None

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)

node4.next = node5
node5.next = node6
node6.next = None

print(node1)
print(node1.next)

print(node4)
"""
