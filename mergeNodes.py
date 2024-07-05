"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
Return the head of the modified linked list.

Example 1:
Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.

Example 2:
Input: head = [0,1,0,3,0,2,2,0]
Output: [1,3,4]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 1 = 1.
- The sum of the nodes marked in red: 3 = 3.
- The sum of the nodes marked in yellow: 2 + 2 = 4.

Constraints:
    The number of nodes in the list is in the range [3, 2 * 10^5].
    0 <= Node.val <= 1000
    There are no two consecutive nodes with Node.val == 0.
    The beginning and end of the linked list have Node.val == 0.

Hint 1
How can you use two pointers to modify the original list into the new list?

Hint 2
Have a pointer traverse the entire linked list, while another pointer looks at a node that is currently being modified.

Hint 3
Keep on summing the values of the nodes between the traversal pointer and the modifying pointer until the former comes across a ‘0’. In that case, the modifying pointer is incremented to modify the next node.

Hint 4
Do not forget to have the next pointer of the final node of the modified list point to null.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.val == 0:
                if head.next is None:  # If the next node after a 0 is None, break the loop
                    prev.next = None
                    break
                prev.next = head
                prev = head
                head = head.next
                while head and head.val != 0:
                    prev.val += head.val
                    head = head.next
                prev.next = None
            else:
                prev = head
                head = head.next
        return dummy.next

def printNodes(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
solution = Solution()
head = solution.mergeNodes(head)
printNodes(head)