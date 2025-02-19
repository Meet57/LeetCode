# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # question in inorder
        # root, left, right
        # need to lowest root in between

        current = root

        # So if the current value is less than P and Q then it must be there in the right side as for BST And vice versa and if any of the P or Q Value matches with the current value it returns as it's obvious that it is the lowest because it is between the two numbers and it is lying above of any P and Q as per BST

# equal thy to means smaller number pehla ayu hot inorder ma

        while current:
            if root.val == p.val or root.val == q.val:
                return root
            # Here the first condition is based on root not the current value because it will check the H cases and the functioning of the logic is there in the last else block where every if statement will fail because either the current value would be equal to P or Q so it will go to the else block and will return the current block

            if current.val < p.val and current.val < q.val:
                current = current.right

            elif current.val > p.val and current.val > q.val:
                current = current.left
            
            else:
                return current