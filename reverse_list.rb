# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def reverse_list(head)
    prev = nil
    while head
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    end
    prev 
end