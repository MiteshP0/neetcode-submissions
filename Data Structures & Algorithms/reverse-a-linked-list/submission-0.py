# O(n) and O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # one rule to rmb: Save first, flip second, advance third.
        prev = None
        curr = head
        while curr: # keep iterating while there nodes
            next_node = curr.next # save rest of list before overwriting curr.next
            curr.next = prev # flip so point curr node backwards to new reversed part
            prev = curr # advance prev to include this node in reversed part
            curr = next_node # advance curr to next node now.
        return prev



        