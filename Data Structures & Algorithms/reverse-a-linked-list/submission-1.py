# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        if head.next is None:
            return head
        
        prevNode = None
        currentNode = head
        
        
        while currentNode is not None:
            
            temp = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = temp
            
        
        return prevNode 