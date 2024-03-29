/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
// var hasCycle = function(head) {
//     let pos = {};
//     let current = head;
//     while(current !== null && current.next >= 0){
//         // console.log(current.next)
//         if (pos[current]){
//             return true;
//         }
//         pos[head] = current;
//         current = head.next;
//     }
//     return false;
// };

var hasCycle = function(head) {
    let fast = head;
    let slow = head;
    while(fast && fast.next){
        fast = fast.next.next;
        slow = slow.next;
        if (fast === slow) return true;
    }
    return false;
};