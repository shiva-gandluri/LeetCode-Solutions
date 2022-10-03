# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not(head and head.next)): #base conditions
            return head
        
        first, second = head, head.next
        
        while(first and second):
            while(first and second and first.val == second.val): #updating Linked List
                first.next, second = second.next, second.next
                
            if(first and second): #iteration steps
                first = first.next
                second = second.next
            
        return head
