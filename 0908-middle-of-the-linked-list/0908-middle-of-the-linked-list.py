# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Again two pointer, faster pointer in end then slower pointer in the mid
        faster = head
        slower = head

        while faster and faster.next:
            faster = faster.next.next
            slower = slower.next

        return slower