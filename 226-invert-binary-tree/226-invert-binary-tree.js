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
 * @return {TreeNode}
 */
// var invertTree = function(root) {
//     const reverseNodes = (node) => {
//         if (node == null){
//             return;
//         }    
//         reverseNodes(node.left);
//         reverseNodes(node.right);
//         let temp = node.left;
//         node.left = node.right;
//         node.right = temp;
//     }
//     reverseNodes(root);
//     return root;
// };

var invertTree = function(root) {
    let st = [root];
    while(st.length > 0){
        let node = st.pop();
        if (node != null){
            let temp = node.left;
            node.left = node.right;
            node.right = temp;
            
            st.push(node.left);
            st.push(node.right);
        }
    }
    return root;
};