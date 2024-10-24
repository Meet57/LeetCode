# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to hold the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists while neither is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Append list1's node to merged list
                list1 = list1.next    # Move to the next node in list1
            else:
                current.next = list2  # Append list2's node to merged list
                list2 = list2.next    # Move to the next node in list2
            current = current.next    # Move current pointer forward

        # Attach the remaining non-empty list (if any)
        current.next = list1 if list1 else list2
        
        return dummy.next  # Return merged list, skipping dummy node