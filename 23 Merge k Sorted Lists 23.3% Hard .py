# https://docs.python.org/3.6/library/heapq.html
# the heap queue algorithm, also known as the priority queue algorithm.
# Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

# To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().

"""
heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.


heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].


heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.

heapq.heapreplace(heap, item)
Pop and return the smallest item from the heap, and also push the new item. The heap size doesn’t change. If the heap is empty, IndexError is raised.

This one step operation is more efficient than a heappop() followed by heappush() and can be more appropriate when using a fixed-size heap. The pop/push combination always returns an element from the heap and replaces it with item.

The value returned may be larger than the item added. If that isn’t desired, consider using heappushpop() instead. Its push/pop combination returns the smaller of the two values, leaving the larger value on the heap.

"""

