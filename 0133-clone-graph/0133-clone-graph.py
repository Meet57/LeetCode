
class Solution:
    def clone(self, node, clones={}):
        if not node:
            return None

        # If node is already cloned, return the clone
        if node in clones:
            return clones[node]

        # It is important to make the node of the graph as it matters further for making the neighbors
        # Create a new clone of the current node
        clone_node = Node(node.val)
        clones[node] = clone_node

        # Clone the neighbors recursively
        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.clone(neighbor, clones))

        return clone_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone(node)
