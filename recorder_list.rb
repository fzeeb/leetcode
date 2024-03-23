=begin
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
=end
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {Void} Do not return anything, modify head in-place instead.
def reorder_list(head)
    # Initialize an array to store the values of the linked list
    arr = []
    # Traverse the linked list and store the values in the array
    while head
        arr << head
        head = head.next
    end
    # Initialize a pointer to the head of the linked list
    head = arr.shift
    # Initialize a variable to store the length of the array
    n = arr.length
    # Traverse the array and reorder the linked list
    (0...n).each do |i|
        if i.even?
            head.next = arr.pop
        else
            head.next = arr.shift
        end
        head = head.next
    end
    # Set the next node of the last node to nil
    head.next = nil
end