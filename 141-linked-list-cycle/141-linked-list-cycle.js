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
//     let cycled = false;
//     let next;
//     let position;
//     let currentPos = 1;
//     while(current !== null && cycled === false){
//         if (pos.includes(position)){
//             cycled = true;
//             return cycled;
//         }
//         current.position = currentPos;
//         currentPos += 1;
//         next = current.next;
//         current = next;
//     }
//     return cycled;
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