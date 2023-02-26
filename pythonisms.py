from functools import wraps


def pretty_print_tree(func):
    """
    Formats tree output.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        visual = ""
        levels = func(*args, **kwargs)
        for level in levels:
            for val in level:
                visual += f"({val}) "
            visual += "-> "
        return visual
    return wrapper


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

    def __iter__(self):
        yield from self.get_values()

    @pretty_print_tree
    def print_levels(self):
        """
        Returns a string showing the values in each level of the tree.
        """
        q = []
        if self.root:
            q.append(self.root)

        levels = []

        while q:
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            levels.append(level)

        return levels

    def __eq__(self, tree2):

        def is_same(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False

            return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)

        return is_same(self.root, tree2.root)

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
