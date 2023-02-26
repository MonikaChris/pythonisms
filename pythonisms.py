class BST:
    """
    Binary Search Tree class that supports inserting and removing nodes, as well as iterating over the nodes in order.
    """

    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        """
        Inserts node with given value in binary search tree. Preserves sorted order. Returns inserted value.
        """
        def insert_node(val, root):
            if not root:
                return Node(val)

            if val < root.val:
                root.left = insert_node(val, root.left)
            elif val > root.val:
                root.right = insert_node(val, root.right)

            return root

        insert_node(value, self.root)
        return value

    def get_values(self):
        """
        Returns an in order list of node values.
        """

        def walk(root, values):
            if not root:
                return None

            walk(root.left, values)
            values.append(root.val)
            walk(root.right, values)

            return values

        return walk(self.root, [])


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
