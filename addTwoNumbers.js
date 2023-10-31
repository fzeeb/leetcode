/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {

  // create a new linked list
  let newList = new ListNode();
  let currentNode = newList;
  let carry = 0;

  // iterate through both lists
  // add the values of the nodes
  // if the sum is greater than 10, carry the 1
  // create a new node with the sum
  // set the current node's next to the new node
  // set the current node to the new node
  // if there is a carry, add it to the sum
  // return the new list
  while (l1 || l2) {
    let sum = 0;
    if (l1) {
      sum += l1.val;
      l1 = l1.next;
    } 
    if (l2) {
      sum += l2.val;
      l2 = l2.next;
    }
    sum += carry;
    carry = 0;
    if (sum >= 10) {
      carry = 1;
      sum -= 10;
    }
    currentNode.next = new ListNode(sum);
    currentNode = currentNode.next;
  }

  if (carry) {
    currentNode.next = new ListNode(carry);
  }

  return newList.next;    
};