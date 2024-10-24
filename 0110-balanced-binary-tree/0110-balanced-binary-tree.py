# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        # So what we did here is we checked the length from left side and right side and then compare it and if it is greater than one that means that the difference between 2 sides of the binary tree is greater than 1 that means it is not a balanced tree so we checked height from either of the side and and checked the difference between them and if it is greater than one we return false otherwise true here we added nonlocal keyword that means it can use the outside result as its local inside the function.

        # How the height is checked is? If root is null then return 0 and increment it on every previous recursion 

        def height(root):
            nonlocal result

            if root == None:
                return 0

            l = height(root.left)
            r = height(root.right)

            if abs(l-r) > 1:
                result = False
            
            return max(l,r)+1
        
        height(root)
        return result