# use min-heap (binary tree)
# min would be start of tree. push/pop O(logn). heapify O(n)
# O(nlogn), O(n) - space
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks) # O(n) 
        total = 0
        # Each merge removes 2 sticks and adds 1, so length shrinks by 1 each
        # iteration. Stop when only one stick remains.
        while len(sticks) > 1:
            x = heapq.heappop(sticks) # smallest
            y = heapq.heappop(sticks) # second smallest
            merged = x + y
            total += merged # keep track total
            heapq.heappush(sticks, merged) # keep push merged value
        return total