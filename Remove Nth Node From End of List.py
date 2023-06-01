class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)#value of dummmy is 0 and after we wikll initialize it to head ctreating a dummmy node at the start  position 
        left = dummy # initializing left to the start ie dummy
        right = head
        while n>0 and right:#when right is not none and n is the position we want to delete the node at 
            right = right.next 
            n-=1#decrementing n after goin forward for right 
        while right :#when right reaches the null left will be at that position where we ant to delete 
            left = left.next 
            right = right.next
            #main thing to delete ie we will skip the node we want to delete 
        left.next = left.next.next
        return dummy.next    
