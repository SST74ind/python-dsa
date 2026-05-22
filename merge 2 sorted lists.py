#time complexity O(n+m) where n and m are the lengths of the two lists
#space complexity O(1) since we are not using any extra space
class Solution(object):
    def mergeTwoLists(self, list1, list2):      
        x=ListNode(0)
        c=x
        while list1 and list2:
            if list1.val<list2.val:
                c.next=list1
                list1=list1.next
            else:
                c.next=list2
                list2=list2.next
            c=c.next
        if list1:
            c.next=list1
        else:
            c.next=list2
        return x.next
#Example usage:
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
#Create two sorted linked lists
list1=ListNode(1,ListNode(2,ListNode(4)))
list2=ListNode(1,ListNode(3,ListNode(4)))
solution=Solution()
merged_list=solution.mergeTwoLists(list1, list2)
#Print the merged linked list
current=merged_list
while current:
    print(current.val)
    current=current.next