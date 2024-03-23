/*
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
*/
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if (!head) {
        return null;
    }
    let list = [];
    let current = head;
    while (current) {
        list.push(current);
        current = current.next;
    }
    let left = 0;
    let right = list.length - 1;
    while (left < right) {
        list[left].next = list[right];
        left++;
        if (left === right) {
            break;
        }
        list[right].next = list[left];
        right--;
    }
    list[left].next = null;
    return head;
};