"""
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.

Example 1:
Input: head = [1,8,9]
Output: [3,7,8]
Explanation: The figure above corresponds to the given linked list which represents the number 189. Hence, the returned linked list represents the number 189 * 2 = 378.

Example 2:
Input: head = [9,9,9]
Output: [1,9,9,8]
Explanation: The figure above corresponds to the given linked list which represents the number 999. Hence, the returned linked list reprersents the number 999 * 2 = 1998.

Constraints:
The number of nodes in the list is in the range [1, 10^4]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

Hint 1
Traverse the linked list from the least significant digit to the most significant digit and multiply each node's value by 2

Hint 2
Handle any carry-over digits that may arise during the doubling process.

Hint 3
If there is a carry-over digit on the most significant digit, create a new node with that value and point it to the start of the given linked list and return it.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # reverse the linked list
      def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
          prev = None
          while head:
              temp = head.next
              head.next = prev
              prev = head
              head = temp
          return prev
    
      # double each node and carry over
      def double(head: Optional[ListNode]) -> Optional[ListNode]:
          carry = 0
          dummy = ListNode(0)
          dummy.next = head
          while head:
              head.val = head.val * 2 + carry
              carry = head.val // 10
              head.val %= 10
              if not head.next and carry:
                  head.next = ListNode(carry)
                  break
              head = head.next
          return dummy.next
      
      # reverse the linked list back
      return reverse(double(reverse(head)))
    
    
print(Solution().doubleIt(ListNode(1, ListNode(8, ListNode(9)))).val) # 3 -> 7 -> 8