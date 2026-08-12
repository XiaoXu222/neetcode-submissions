# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        
        cur3 = None
        prev3 = None
        head = None
        count = 0

        while cur1 or cur2:
            if ((cur1 and cur2) and (cur1.val <= cur2.val)) or cur2 == None:
                cur3 = ListNode(cur1.val)
                
                if count == 0:
                    head = cur3
                else:
                    prev3.next = cur3

                prev3 = cur3
                cur1 = cur1.next
            elif ((cur1 and cur2) and (cur1.val > cur2.val)) or cur1 == None:
                cur3 = ListNode(cur2.val)
                
                if count == 0:
                    head = cur3
                else:
                    prev3.next = cur3

                prev3 = cur3
                cur2 = cur2.next

            count += 1

        return head


        