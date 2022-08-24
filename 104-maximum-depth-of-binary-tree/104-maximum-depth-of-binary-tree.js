/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

var maxDepth = function(root) {
    if (root == null) {
        return 0;
    }
    let left = maxDepth(root.left);
    let right = maxDepth(root.right);
    // let pick = left > right ? left + 1 : right + 1;
    let max = 0;
    if (left > right) {
        max = left + 1;
    } else {
        max = right + 1;
    }
    return max;
}