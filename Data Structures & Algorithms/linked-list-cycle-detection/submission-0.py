# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        cur = head
        while cur:
            cur.val = [cur.val, index]
            if cur.next and isinstance(cur.next.val, list):
                return True
            cur = cur.next
            index += 1
        return False

        