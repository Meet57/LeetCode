class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, min, max):
            if not node:
                return True
            
            if (min is not None and node.val <= min) or (max is not None and node.val >= max):
                return False
            
            # Here we are not checking the node left and right
            # Instead we are checking the values, for example for left node the current node value must be bigger and vise versa
            return validate(node.left,min,node.val) and validate(node.right,node.val,max)

        return validate(root, None, None)