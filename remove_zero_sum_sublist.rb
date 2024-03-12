=begin
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.
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
# @return {ListNode}
def remove_zero_sum_sublists(head)
  dummy = ListNode.new(0)
  dummy.next = head
  map = {}
  sum = 0
  current = dummy
  while current
    sum += current.val
    map[sum] = current
    current = current.next
  end
  sum = 0
  current = dummy
  while current
    sum += current.val
    current.next = map[sum].next
    current = current.next
  end
  dummy.next
end

head = [1,2,-3,3,1]
remove_zero_sum_sublists(head) # [3,1]