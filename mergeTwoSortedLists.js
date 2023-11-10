/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
  // create a new list
  let newList = new ListNode();

  // create a current node
  let currentNode = newList;

  // iterate through both lists
  while (list1 !== null || list2 !== null) {
    // compare the values of the nodes
    if (list1 === null || (list2 !== null && list1.val > list2.val)) {
      // add the smaller value to the new list
      currentNode.next = new ListNode(list2.val);
      // move the pointer of the smaller value's list
      list2 = list2.next;
    } else {
      currentNode.next = new ListNode(list1.val);
      list1 = list1.next;
    }
    // set the current node's next to the new node
    currentNode = currentNode.next;
  }

  // return the new list
  return newList.next;
};