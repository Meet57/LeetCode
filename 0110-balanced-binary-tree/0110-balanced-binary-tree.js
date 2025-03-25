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
 * @return {boolean}
 */
var isBalanced = function(root) {
    var result = true

    var checkRoot = root => {
        if(root == null){
            return 0
        }

        let l = checkRoot(root.left)
        let r = checkRoot(root.right)

        if(Math.abs(l-r) > 1){
            result = false
        }

        return Math.max(l,r) + 1
    }

    checkRoot(root)
    return result 
};