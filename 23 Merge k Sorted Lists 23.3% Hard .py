# use heap to solve this problem
# memorize this question!!

# https://docs.python.org/3.6/library/heapq.html
# the heap queue algorithm, also known as the priority queue algorithm.
# Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

# To create a heap, use a list initialized to [], or
# you can transform a populated list into a heap via function heapify().

"""
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.


heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


        
import heapq
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy

        heap = []
        for list in lists:
            if list:
                heapq.heappush(heap, (list.val, list))
                # Heap elements can be tuples. This is useful for assigning comparison values (such as task priorities) alongside the main record being tracked.

        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next

            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next

