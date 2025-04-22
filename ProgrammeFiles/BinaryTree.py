
# Implement Binary Tree Implementation


#Create a Tree Node

# binary_tree_module.py

# Tree Node Definition
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Binary Tree Class Definition
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.val:
            if not node.left:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if not node.right:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return self._inorder(node.left) + [node.val] + self._inorder(node.right) if node else []

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        return [node.val] + self._preorder(node.left) + self._preorder(node.right) if node else []

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        return self._postorder(node.left) + self._postorder(node.right) + [node.val] if node else []

    def search(self, target):
        return self._search(self.root, target)

    def _search(self, node, target):
        if not node:
            return False
        elif node.val == target:
            return True
        elif node.val < target:
            return self._search(node.right, target)
        else:
            return self._search(node.left, target)

    def Height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        left = self._height(node.left)
        right = self._height(node.right)
        return 1 + max(left, right)

    def delete_node(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            small_val = self.min_currentVal(node.right)
            node.val = small_val.val
            node.right = self._delete(node.right, small_val.val)
        return node

    def min_currentVal(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    
    


