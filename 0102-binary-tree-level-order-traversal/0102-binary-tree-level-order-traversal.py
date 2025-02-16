# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Here we initialize a root and what we do further is pop one element from the root and then checking it left and right and adding to a queue and the root would be appended to the levels so the further queue would be another level and if there is any null it will just skip that part

        # Initialize a queue with the root node.
        queue = [root]
        res = []

        while queue:
            # Process each level:
            level_root = len(queue)
            level_values = []

            # Get the number of nodes at the current level.
            for _ in range(level_root):
                node = queue.pop(0)
                level_values.append(node.val)
                # Traverse these nodes and store their values.
                # Add their left and right children (if present) to the queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_values)
            # Continue until the queue is empty.   

        return res
        