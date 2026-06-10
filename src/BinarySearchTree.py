
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if not current.left:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder(self):
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.value)
                traverse(node.right)
        traverse(self.root)
        return result
    
    def delete(self, value):
        def delete_node(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = self.min_value_node(node.right)
                node.value = temp.value
                node.right = delete_node(node.right, temp.value)
            return node
        self.root = delete_node(self.root, value)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    print(bst.inorder())  # Output: [3, 5, 7]
    print(bst.search(3))  # Output: True
    print(bst.search(4))  # Output: False
    bst.delete(3)
    print(bst.inorder())  # Output: [5, 7]