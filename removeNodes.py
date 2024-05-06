from typing import Optional
"""
You are given the head of a linked list.
Remove every node which has a node with a greater value anywhere to the right side of it.
Return the head of the modified linked list.

Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.

Node 13 is to the right of node 5.

Node 13 is to the right of node 2.

Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.

Constraints:
The number of the nodes in the given list is in the range [1, 10^5].
1 <= Node.val <= 10^5

Hint 1
Iterate on nodes in reversed order.

Hint 2
When iterating in reversed order, save the maximum value that was passed before.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the linked list
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        # remove the nodes with a greater value to the right
        prev = None
        current = head
        max_val = head.val
        while current:
            if current.val < max_val:
                if prev:
                    prev.next = current.next
            else:
                max_val = current.val
                prev = current
            current = current.next
        # reverse the linked list back
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        return head