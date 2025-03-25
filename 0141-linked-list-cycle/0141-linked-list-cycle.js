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
var hasCycle = function(head) {
    if(head == null || head.next == null){
        return false
    }

    let x = head
    let y = head

    while(x && x.next){
        y = y.next
        x = x.next.next

        if(x==y){
            return true
        }
    }

    return false
};