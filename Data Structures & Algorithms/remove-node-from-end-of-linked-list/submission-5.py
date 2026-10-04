# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = n - 1
        
        fast, slow = head, head

        for i in range(k):
            fast = fast.next
        
        prev = None
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if not prev:
            tmp = slow.next
            slow.next = None
            head = tmp
        else:
            prev.next = slow.next
            slow.next = None

        # if slow == fast:
        #     if not prev:
        #         return None
        #     else:
        #         prev.next = None
        # else:
        
        #     if prev:
        #         prev.next = slow.next
        #         slow.next = None
        #     else:
        #         tmp = slow.next
        #         slow.next = None
        #         head = tmp
            
        
        return head
            
        