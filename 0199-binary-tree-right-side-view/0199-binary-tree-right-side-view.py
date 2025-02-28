class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        onlyRight = []
        queue = [root]  # Use the node itself, not just the value
        onlyRight.append(root.val)

        while queue:
            temp = []
            furtherNodes = []

            # Traverse nodes at the current level
            for node in queue:
                if node.left:
                    temp.append(node.left.val)
                    furtherNodes.append(node.left)
                if node.right:
                    temp.append(node.right.val)
                    furtherNodes.append(node.right)
            
            # Append the last element (rightmost) of the current level
            onlyRight.append(temp[-1]) if temp else None
            
            # Move to the next level
            queue = furtherNodes

        return onlyRight
