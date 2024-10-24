# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
        
        x = head
        y = head

        # So this is called two pointer method what we do is one pointer moves faster and the other moves slower, If the pointer value matches it means the linked list is circular and if it doesn't matches that means the faster node has already reached the end that means there is a definite end and there is no cycle

        #  What to make sure in this question is if the value matches we have to return true and we have to loop with the faster node

        # Don't compare the value otherwise the link list may have same value again compare the nodes

        while y and y.next:            
            x = x.next
            y = y.next.next

            if x == y:
                return True
            
        return False