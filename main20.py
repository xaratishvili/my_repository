class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def LeafNodes(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value)
        self.LeafNodes(node.left)
        self.LeafNodes(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

tree = BinaryTree(root)
tree.LeafNodes(root)

