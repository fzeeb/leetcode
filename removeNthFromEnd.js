/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    // create a dummy node
    const dummy = new ListNode(0);

    // set the dummy node's next to the head
    dummy.next = head;

    // create a slow pointer and set it to the dummy node
    let slow = dummy;

    // create a fast pointer and set it to the dummy node
    let fast = dummy;

    // loop while the fast pointer is not null
    while (fast !== null) {
        // check if n is less than 0
        if (n < 0) {
            // increment the slow pointer
            slow = slow.next;
        }

        // decrement n
        n--;

        // increment the fast pointer
        fast = fast.next;
    }

    // set the slow pointer's next to the slow pointer's next's next
    slow.next = slow.next.next;

    // return the dummy node's next
    return dummy.next;
};