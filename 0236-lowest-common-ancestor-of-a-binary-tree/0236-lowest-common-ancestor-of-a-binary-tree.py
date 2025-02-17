class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

        # This problem is similar to the lowest common ancestor of a binary search tree where the binary search tree ensures that the left side is the smaller and the right side is the bigger one here in the binary tree it only ensures that every node has two children not more than that

        if not root or root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)

        # There are basically two conditions either the P and Q is the root while recursion or either of them is the root so if it is P or cube being the root value it will be returned automatically from the upper base case scenario of recursion otherwise what will happen is if either of P and Q is the root the L and R either of them would be none which represents that the function will return the other non nun value which is basically the above ancestor and it follows till the root a chilled root of the binary tree which has the other side as None value
        if l and r:
            return root

        return l or r