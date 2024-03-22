# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Boolean}
def is_palindrome(head)
    # Initialize an array to store the values of the linked list
    arr = []
    # Traverse the linked list and store the values in the array
    while head
        arr << head.val
        head = head.next
    end
    # Check if the array is equal to the array in reverse
    arr == arr.reverse 
end