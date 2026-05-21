#time complexity: O(n)
#space complexity: O(1)
class Solution(object):
    def reverseList(self, head):
        x, y= head, None
        while x:
            nxt=x.next
            x.next=y
            y=x
            x=nxt
        return y
#Example usage:
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
# Create a linked list: 1 -> 2 -> 3 -> None
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
solution=Solution()
reversed_head=solution.reverseList(head)
# Print the reversed linked list
current=reversed_head
while current:
    print(current.val)  # Output: 3, 2, 1
    current=current.next