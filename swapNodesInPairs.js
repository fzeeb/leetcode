/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
  // if head is null or head.next is null, return head
  if (head === null || head.next === null) return head;
  // create a new list
  let newList = new ListNode();
  // create a current node
  let currentNode = newList;
  // iterate through the list
  while (head !== null && head.next !== null) {
    // swap the values of the nodes
    currentNode.next = new ListNode(head.next.val);
    currentNode.next.next = new ListNode(head.val);
    // move the pointer of the list
    head = head.next.next;
    // move the pointer of the new list
    currentNode = currentNode.next.next;
  }
  // if head is not null, add it to the new list
  if (head !== null) currentNode.next = new ListNode(head.val);
  // return the new list
  return newList.next;
};